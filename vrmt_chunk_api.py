import os
from flask import Flask, request, jsonify
from markdown import markdown
from bs4 import BeautifulSoup
from uuid import uuid4
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()  # Load .env if running locally

# === Load API keys from environment ===
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

# === Initialize OpenAI and Pinecone clients ===
openai = OpenAI(api_key=OPENAI_API_KEY)
pc = Pinecone(api_key=PINECONE_API_KEY)

INDEX_NAME = "vrmt-docs"
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)

# === STEP 1: CHUNKING ===
def load_chunks(md_file):
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    html = markdown(md_text)
    soup = BeautifulSoup(html, "html.parser")

    chunks = []
    current_section = []
    title = ""

    for el in soup.find_all(["h2", "h3", "p", "ul", "ol"]):
        if el.name in ["h2", "h3"]:
            if current_section:
                chunks.append({"title": title, "text": "\n".join(current_section)})
                current_section = []
            title = el.get_text()
        else:
            current_section.append(el.get_text())

    if current_section:
        chunks.append({"title": title, "text": "\n".join(current_section)})

    return chunks

# === STEP 2: EMBED & UPSERT ===
def embed_and_upload(chunks):
    # Clear all existing vectors from the index to avoid duplicates
    index.delete(delete_all=True)

    vectors = []
    for chunk in chunks:
        text = chunk["text"]
        title = chunk["title"]
        embedding = openai.embeddings.create(
            model="text-embedding-3-small",
            input=[text]
        ).data[0].embedding

        vector = {
            "id": str(uuid4()),
            "values": embedding,
            "metadata": {
                "title": title,
                "text": text
            }
        }
        vectors.append(vector)

    index.upsert(vectors)
    return len(vectors)

# === AUTO-CHUNK ON DEPLOY ===
try:
    md_path = "vr-system.md"
    if os.path.exists(md_path):
        chunks = load_chunks(md_path)
        print(f"Loaded {len(chunks)} chunks. Uploading to Pinecone...")
        count = embed_and_upload(chunks)
        print(f"Uploaded {count} chunks.")
    else:
        print(f"Markdown file '{md_path}' not found, skipping chunking.")
except Exception as e:
    print(f"Auto-chunking failed: {e}")

# === STEP 3: SEARCH ENDPOINT ===
app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Missing query"}), 400

    embedding = openai.embeddings.create(
        model="text-embedding-3-small",
        input=[query]
    ).data[0].embedding

    results = index.query(vector=embedding, top_k=5, include_metadata=True)
    return jsonify([match["metadata"] for match in results["matches"]])
