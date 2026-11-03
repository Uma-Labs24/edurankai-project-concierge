MOCK_ORDERS={'DEMO-1001':{'order_id':'DEMO-1001','status':'shipped','eta':'2026-11-08'}}
class MockOrderAPI:
 def __init__(self,mode='success'): self.mode=mode
 def get_order(self,oid):
  if self.mode=='timeout': raise TimeoutError()
  if self.mode=='service_error': raise RuntimeError()
  if self.mode=='malformed': return {'bad':'shape'}
  return MOCK_ORDERS.get(oid)
def lookup_order(order_id,api=None):
 api=api or MockOrderAPI()
 if not isinstance(order_id,str) or not order_id.strip(): return {'status':'invalid_request','message':'Please provide an order ID.'}
 try: data=api.get_order(order_id.strip().upper())
 except TimeoutError: return {'status':'timeout','message':'Order lookup timed out.'}
 except Exception: return {'status':'service_error','message':'Order service unavailable.'}
 if data is None: return {'status':'not_found','message':'No demo order found.'}
 if not isinstance(data,dict) or not all(isinstance(data.get(k),str) for k in ('order_id','status','eta')): return {'status':'malformed_response','message':'Invalid order response.'}
 return {'status':'success','message':'Demo order found.','order':data}
