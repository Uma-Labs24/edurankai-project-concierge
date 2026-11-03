from .policies import answer
from .orders import lookup_order
from .handoff import create_handoff,should_escalate
def main():
 print('Project Concierge Day 3 demo'); choice=input('1 policy / 2 mock order: ').strip()
 if choice=='1':
  q=input('Question: '); r=answer(q); print(r)
  if should_escalate(r): print('Handoff ticket',create_handoff(r.get('reason') or r['status'],q,r.get('citations'))['ticket_id'])
 elif choice=='2':
  oid=input('Demo order ID (DEMO-1001): '); r=lookup_order(oid); print(r)
  if r['status']!='success': print('Handoff ticket',create_handoff(r['status'],f'Order {oid}',order_context=r)['ticket_id'])
 else: print('Choose 1 or 2')
if __name__=='__main__':main()
