import json,re
from pathlib import Path
from .retrieval import ROOT,ImprovedRetriever
INDEX=ROOT/'docs'/'policy_versions.json'
def metadata(): return json.loads(INDEX.read_text(encoding='utf-8')) if INDEX.exists() else {'policies':[]}
def conflicts():
 by={}
 for row in metadata().get('policies',[]):
  if row.get('status','current')=='current': by.setdefault(row.get('document_id'),[]).append(row)
 return {k:v for k,v in by.items() if len(v)>1}
def answer(question,retriever=None,k=3):
 ret=retriever or ImprovedRetriever(); hits=ret.search(question,k)
 if not hits: return {'status':'abstained','answer':'Insufficient evidence. Please ask a human reviewer.','citations':[],'reason':'no_retrieved_evidence'}
 if any(h['id'] in conflicts() for h in hits): return {'status':'escalated','answer':'Conflicting current policy versions need human review.','citations':[],'reason':'policy_version_conflict'}
 terms=set(re.findall(r'[a-z0-9]+',question.lower())); best=hits[0]; overlap=terms&set(re.findall(r'[a-z0-9]+',(best['title']+' '+best['text']).lower()))
 if len(overlap)<2 or best['score']<.05: return {'status':'abstained','answer':'Insufficient reliable evidence in demo documents. Please contact a human reviewer.','citations':[],'reason':'insufficient_evidence'}
 rows=[x for x in metadata().get('policies',[]) if x.get('document_id')==best['id'] and x.get('status','current')=='current']; row=rows[-1] if rows else {}
 return {'status':'answered','answer':' '.join(best['text'].split())[:500],'citations':[{'document_id':best['id'],'source':row.get('source','Local demo document'),'version':row.get('version','unknown'),'effective_date':row.get('effective_date','unspecified')}],'reason':None}
