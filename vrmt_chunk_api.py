import os
import re
from flask import Flask, request, jsonify
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
NAMESPACE = "default"  # Explicit namespace

# === Create serverless index if it doesn't exist ===
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)

# === STEP 1: CHUNKING BASED ON MARKDOWN HEADINGS ===
def load_chunks(md_file):
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    chunks = []
    current_chunk_lines = []
    current_title = "Untitled"
    heading_stack = []

    def flush_chunk():
        nonlocal current_chunk_lines, current_title
        if current_chunk_lines:
            chunks.append({
                "title": current_title,
                "text": "".join(current_chunk_lines).strip()
            })
            current_chunk_lines = []

    for line in lines:
        heading_match = re.match(r"^(#{1,6})\s+(.*)", line)
        if heading_match:
            flush_chunk()
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()

            # Adjust heading stack
            if level == 1:
                heading_stack = [title]
            else:
                heading_stack = heading_stack[:level - 1] + [title]

            current_title = " > ".join(heading_stack)
        else:
            current_chunk_lines.append(line)

    flush_chunk()
    return chunks

# === STEP 2: EMBED & UPSERT TO PINECONE ===
def embed_and_upload(chunks):
    try:
        index.delete(delete_all=True, namespace=NAMESPACE)
        print(f"✅ Cleared existing vectors in namespace '{NAMESPACE}'")
    except Exception as e:
        print(f"⚠️ Could not delete existing vectors: {e}")

    vectors = []
    for chunk in chunks:
        text = chunk["text"].strip()
        title = chunk["title"]

        if not text:
            continue

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

    print(f"Uploading {len(vectors)} valid chunks to Pinecone...")
    index.upsert(vectors=vectors, namespace=NAMESPACE)
    print("✅ Upload complete.")
    return len(vectors)

# === AUTO-CHUNK ON DEPLOY ===
try:
    md_path = "vr-system.md"
    if os.path.exists(md_path):
        chunks = load_chunks(md_path)

        # Debug file
        with open("chunked_context_debug.txt", "w", encoding="utf-8") as dbg:
            for chunk in chunks:
                dbg.write(f"--- {chunk['title']} ---\n{chunk['text']}\n\n")

        print(f"Loaded {len(chunks)} structured chunks. Uploading to Pinecone...")
        count = embed_and_upload(chunks)
        print(f"✅ Uploaded {count} chunks.")
    else:
        print(f"⚠️ Markdown file '{md_path}' not found, skipping chunking.")
except Exception as e:
    print(f"❌ Auto-chunking failed: {e}")

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

    results = index.query(
        vector=embedding,
        top_k=5,
        include_metadata=True,
        namespace=NAMESPACE
    )
    return jsonify([match["metadata"] for match in results["matches"]])

