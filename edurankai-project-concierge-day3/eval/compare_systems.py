import json,sys,time,statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from concierge.retrieval import load_documents,Day1TfidfRetriever,ImprovedRetriever
from concierge.policies import answer
def main():
 qs=json.loads((ROOT/'eval/questions.json').read_text());docs=load_documents();out={}
 for name,ret in [('Day 1 baseline',Day1TfidfRetriever(docs)),('Improved Day 2/3',ImprovedRetriever(docs))]:
  rec=[];cov=0;ab=0;lat=[]
  for x in qs:
   t=time.perf_counter();hits=ret.search(x['question'],3);lat.append((time.perf_counter()-t)*1000);gold=x['relevant_doc'];rec.append(1 if gold is None or any(h['id']==gold for h in hits) else 0)
   if name=='Day 1 baseline':cov+=bool(hits)
   else:r=answer(x['question'],ret);cov+=bool(r['citations']);ab+=r['status']=='abstained'
  out[name]={'recall_at_3':round(sum(rec)/len(rec),4),'citation_evidence_coverage':round(cov/len(qs),4) if name!='Day 1 baseline' else 'unavailable_baseline_has_no_citations','abstention_count':ab if name!='Day 1 baseline' else 'not_implemented','retrieval_average_latency_ms':round(statistics.mean(lat),4),'question_count':len(qs)}
 report={'note':'Actual local run on small fictional labelled set; not a formal quality guarantee.','systems':out};(ROOT/'reports/system_comparison.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
if __name__=='__main__':main()
