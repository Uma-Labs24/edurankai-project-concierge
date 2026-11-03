from pathlib import Path
import re, math
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'data'/'documents'
def tokenize(s): return re.findall(r"[a-z0-9]+",s.lower())
def load_documents():
 return [{'id':p.stem,'title':p.stem.replace('_',' ').title(),'text':p.read_text(encoding='utf-8')} for p in sorted(DOCS.glob('*.md'))]
class Day1TfidfRetriever:
 def __init__(self,documents=None):
  self.documents=documents or load_documents(); toks=[tokenize(d['title']+' '+d['text']) for d in self.documents]; n=len(toks); df={}
  for ts in toks:
   for t in set(ts): df[t]=df.get(t,0)+1
  self.idf={t:math.log((1+n)/(1+c))+1 for t,c in df.items()}; self.vec=[]
  for ts in toks:
   cnt={}
   for t in ts: cnt[t]=cnt.get(t,0)+1
   v={t:(1+math.log(c))*self.idf[t] for t,c in cnt.items()}; norm=math.sqrt(sum(x*x for x in v.values())) or 1; self.vec.append({t:x/norm for t,x in v.items()})
 def search(self,q,k=3):
  cnt={}
  for t in tokenize(q): cnt[t]=cnt.get(t,0)+1
  v={t:(1+math.log(c))*self.idf[t] for t,c in cnt.items() if t in self.idf}; norm=math.sqrt(sum(x*x for x in v.values())) or 1; v={t:x/norm for t,x in v.items()}
  scored=[(sum(x*vec.get(t,0) for t,x in v.items()),d) for d,vec in zip(self.documents,self.vec)]; scored.sort(key=lambda x:x[0],reverse=True)
  return [{'score':round(s,6),**d} for s,d in scored[:k] if s>0]
class ImprovedRetriever(Day1TfidfRetriever):
 def search(self,q,k=3):
  terms=set(tokenize(q)); phrase=' '.join(tokenize(q)); rows=[]
  for r in super().search(q,len(self.documents)):
   body=' '.join(tokenize(r['title']+' '+r['text'])); boost=.12*len(terms&set(tokenize(r['title'])))+(.2 if phrase and phrase in body else 0); r['score']=round(r['score']+boost,6); rows.append(r)
  rows.sort(key=lambda x:x['score'],reverse=True); return rows[:k]
