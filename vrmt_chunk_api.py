import os
from flask import Flask, request, jsonify
from markdown import markdown
from bs4 import BeautifulSoup
from uuid import uuid4
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec

# === CONFIGURATION ===
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
INDEX_NAME = "vrmt-docs"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI and Pinecone
openai = OpenAI(api_key=OPENAI_API_KEY)
pc = Pinecone(api_key=PINECONE_API_KEY)
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

if __name__ == "__main__":
    chunks = load_chunks("vr-system.md")
    print(f"Loaded {len(chunks)} chunks. Uploading to Pinecone...")
    count = embed_and_upload(chunks)
    print(f"Uploaded {count} chunks.")
    app.run(port=5000)
