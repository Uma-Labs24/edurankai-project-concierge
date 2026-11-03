import json,sys,time,statistics,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from concierge.retrieval import load_documents,Day1TfidfRetriever,ImprovedRetriever
from concierge.policies import answer
def stats(v):
 s=sorted(v); p=s[max(0,math.ceil(.95*len(s))-1)] if s else None
 return {'count':len(v),'average_ms':round(statistics.mean(v),4) if v else None,'median_ms':round(statistics.median(v),4) if v else None,'p95_ms':round(p,4) if p is not None else None}
def main():
 qs=json.loads((ROOT/'eval/questions.json').read_text()); docs=load_documents(); b=Day1TfidfRetriever(docs); im=ImprovedRetriever(docs); bt=[];it=[];at=[]
 for _ in range(30):
  for x in qs:
   t=time.perf_counter();b.search(x['question']);bt.append((time.perf_counter()-t)*1000)
   t=time.perf_counter();im.search(x['question']);it.append((time.perf_counter()-t)*1000)
   t=time.perf_counter();answer(x['question'],im);at.append((time.perf_counter()-t)*1000)
 cost=(500*.50+250*1.50)/1_000_000
 r={'mode':'local_mock_no_paid_llm','samples_per_question':30,'question_count':len(qs),'measurements':{'day1_retrieval':stats(bt),'improved_retrieval':stats(it),'local_answer_pipeline':stats(at)},'cost_estimate':{'status':'illustrative_not_actual_charges','assumption':'Hypothetical 500 input/250 output tokens; assumed USD 0.50/1M input and USD 1.50/1M output; no API call.','estimated_usd_per_query':cost,'actual_api_cost_usd':None}}
 (ROOT/'reports/benchmark_results.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
if __name__=='__main__':main()
