"""Small source-aware document store with policy version metadata."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = ROOT / "data" / "documents"
POLICY_INDEX = ROOT / "docs" / "policy_versions.json"

def load_policy_index():
    if not POLICY_INDEX.exists():
        return []
    return json.loads(POLICY_INDEX.read_text(encoding="utf-8"))

def load_documents():
    """Load Markdown documents and attach source/version metadata."""
    docs = []
    index = load_policy_index()
    policy_by_file = {item["file"]: item for item in index}
    for path in sorted(DOCUMENTS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta = policy_by_file.get(path.name, {})
        docs.append({
            "id": path.stem,
            "title": path.stem.replace("_", " ").title(),
            "text": text,
            "source": meta.get("source", f"Local project document: {path.name}"),
            "version": meta.get("version", "1.0"),
            "effective_date": meta.get("effective_date", "not specified"),
        })
    return docs

def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def retrieve(question, documents=None, limit=3):
    """Simple transparent keyword-overlap retrieval; not an embedding model."""
    documents = documents if documents is not None else load_documents()
    question_terms = tokenize(question)
    scored = []
    for doc in documents:
        doc_terms = tokenize(doc["title"] + " " + doc["text"])
        score = len(question_terms & doc_terms)
        if score:
            scored.append((score, doc))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [doc for _, doc in scored[:limit]]
