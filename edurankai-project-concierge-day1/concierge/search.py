import argparse,json
from pathlib import Path
from .chunking import Chunk
from .retrieval import TfidfRetriever
ROOT=Path(__file__).resolve().parents[1]
INDEX=ROOT/"reports"/"day1_chunks.json"
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--top-k",type=int,default=3)
    args=parser.parse_args()
    if not INDEX.exists(): raise SystemExit("Index missing. Run python -m concierge.build_index")
    rows=json.loads(INDEX.read_text(encoding="utf-8"))
    chunks=[Chunk(**r) for r in rows]
    for rank,r in enumerate(TfidfRetriever(chunks).search(args.query,args.top_k),1):
        print(f"\\n[{rank}] score={r['score']:.4f} | {r['source']} | {r['chunk_id']}\\n{r['text']}")
if __name__=="__main__": main()
