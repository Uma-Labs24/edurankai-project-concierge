import json
from pathlib import Path
from statistics import mean
from .chunking import load_documents,make_chunks
from .retrieval import TfidfRetriever
ROOT=Path(__file__).resolve().parents[1]
def main():
    docs=load_documents(ROOT/"data"/"documents")
    if not docs: raise SystemExit("Add corpus documents to data/documents first.")
    retriever=TfidfRetriever(make_chunks(docs))
    cases=json.loads((ROOT/"eval"/"day1_questions.json").read_text(encoding="utf-8"))
    rows=[]; hits=[]; rr_values=[]
    for case in cases:
        found=retriever.search(case["question"],3)
        expected=set(case.get("expected_sources",[]))
        ranks=[n for n,item in enumerate(found,1) if item["source"] in expected]
        rr=1/min(ranks) if ranks else 0.0
        hits.append(bool(ranks)); rr_values.append(rr)
        rows.append({"id":case["id"],"question":case["question"],"expected_sources":sorted(expected),
                     "retrieved_sources":[x["source"] for x in found],"hit_at_3":bool(ranks),"reciprocal_rank":rr})
    report={"evaluation_type":"retrieval source-hit proxy; not answer correctness",
            "documents":len(docs),"chunks":len(retriever.chunks),"questions":len(cases),
            "hit_rate_at_3":mean(hits) if hits else 0,"mean_reciprocal_rank":mean(rr_values) if rr_values else 0,
            "results":rows,"caution":"Validate expected source labels against actual corpus."}
    out=ROOT/"reports"/"day1_baseline.json"; out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="results"},indent=2)); print(f"Detailed results: {out}")
if __name__=="__main__": main()
