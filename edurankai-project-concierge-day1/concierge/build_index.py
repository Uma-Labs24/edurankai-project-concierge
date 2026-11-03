import json
from pathlib import Path
from .chunking import load_documents, make_chunks
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/"data"/"documents"
OUT=ROOT/"reports"/"day1_chunks.json"
def main():
    docs=load_documents(DOCS)
    if not docs: raise SystemExit(f"No .txt/.md files found in {DOCS}. Add the assessment corpus.")
    chunks=make_chunks(docs)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps([c.__dict__ for c in chunks],ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"Loaded {len(docs)} documents; created {len(chunks)} chunks. Saved {OUT}")
if __name__=="__main__": main()
