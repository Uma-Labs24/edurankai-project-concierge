import json,uuid
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; QUEUE=ROOT/'reports'/'human_handoff_queue.jsonl'
def create_handoff(reason,question,evidence=None,order_context=None):
 ticket={'ticket_id':str(uuid.uuid4()),'reason':reason,'question':question,'evidence':evidence or [],'order_context':order_context,'status':'pending_human_review','notice':'Local queue only; no support agent contacted.'}; QUEUE.parent.mkdir(exist_ok=True)
 with QUEUE.open('a',encoding='utf-8') as f:f.write(json.dumps(ticket)+'\n')
 return ticket
def should_escalate(result): return result.get('status') in {'abstained','escalated','error','not_found','timeout','service_error','malformed_response'}
