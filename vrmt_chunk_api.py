import os
import re
from flask import Flask, request, jsonify
from uuid import uuid4
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

# === Load API keys ===
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

# === Initialize clients ===
openai = OpenAI(api_key=OPENAI_API_KEY)
pc = Pinecone(api_key=PINECONE_API_KEY)

INDEX_NAME = "vrmt-docs"
NAMESPACE = "default"

if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)

# === Helper: extract simple focus_target tag ===
def infer_focus_target_from_text(text):
    known_targets = ["bottle tester", "gob distributor", "i.s. machine", "lehr", "emhart", "control panel"]
    for t in known_targets:
        if t in text.lower():
            return t
    return None

# === STEP 1: Markdown Chunking ===
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
            full_text = "".join(current_chunk_lines).strip()
            if len(full_text.split()) < 50:
                current_chunk_lines = []
                return  # skip too small
            target = infer_focus_target_from_text(full_text)
            chunks.append({
                "title": current_title,
                "text": full_text,
                "target": target or "general"
            })
            current_chunk_lines = []

    for line in lines:
        heading_match = re.match(r"^(#{1,6})\s+(.*)", line)
        if heading_match:
            flush_chunk()
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            heading_stack = heading_stack[:level - 1] + [title]
            current_title = " > ".join(heading_stack)
        else:
            current_chunk_lines.append(line)

    flush_chunk()
    return chunks

# === STEP 2: Upload to Pinecone ===
def embed_and_upload(chunks):
    try:
        index.delete(delete_all=True, namespace=NAMESPACE)
        print(f"✅ Cleared existing vectors in namespace '{NAMESPACE}'")
    except Exception as e:
        print(f"⚠️ Could not delete existing vectors: {e}")

    vectors = []
    for chunk in chunks:
        text = chunk["text"]
        title = chunk["title"]
        target = chunk.get("target", "general")

        embedding = openai.embeddings.create(
            model="text-embedding-3-small",
            input=[text]
        ).data[0].embedding

        vectors.append({
            "id": str(uuid4()),
            "values": embedding,
            "metadata": {
                "title": title,
                "text": text,
                "target": target
            }
        })

    print(f"Uploading {len(vectors)} valid chunks to Pinecone...")
    index.upsert(vectors=vectors, namespace=NAMESPACE)
    print("✅ Upload complete.")
    return len(vectors)

# === AUTO-UPLOAD ===
try:
    md_path = "vr-system.md"
    if os.path.exists(md_path):
        chunks = load_chunks(md_path)

        with open("chunked_context_debug.txt", "w", encoding="utf-8") as dbg:
            for chunk in chunks:
                dbg.write(f"--- {chunk['title']} ---\nTarget: {chunk['target']}\n{chunk['text']}\n\n")

        print(f"Loaded {len(chunks)} structured chunks. Uploading to Pinecone...")
        count = embed_and_upload(chunks)
        print(f"✅ Uploaded {count} chunks.")
    else:
        print(f"⚠️ Markdown file '{md_path}' not found, skipping chunking.")
except Exception as e:
    print(f"❌ Auto-chunking failed: {e}")

# === STEP 3: Search API ===
app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")
    focus_target = data.get("focus_target", "").lower().strip()

    # Rewrite vague queries
    if query.lower().strip() in ["yes", "yes please", "yes please. tell me how to use it."] and focus_target:
        query = f"How do I use the {focus_target}?"

    # Get embedding
    embedding = openai.embeddings.create(
        model="text-embedding-3-small",
        input=[query]
    ).data[0].embedding

    # Apply filter if focus_target is provided
    pinecone_filter = {}
    if focus_target:
        pinecone_filter["target"] = {"$eq": focus_target}

    results = index.query(
        vector=embedding,
        top_k=5,
        include_metadata=True,
        namespace=NAMESPACE,
        filter=pinecone_filter if pinecone_filter else None
    )

    # Format result chunks
    formatted_chunks = []
    for match in results["matches"]:
        meta = match.get("metadata", {})
        title = meta.get("title", "Untitled").strip()
        text = meta.get("text", "").strip()
        if text:
            formatted_chunks.append(f"--- {title} ---\n{text}")

    reference_info = "\n\n".join(formatted_chunks)

    return jsonify({
        "reference_info": reference_info,
        "match_count": len(formatted_chunks),
        "applied_filter": pinecone_filter
    })



