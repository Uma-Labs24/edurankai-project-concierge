import unittest
from concierge.retrieval import Day1TfidfRetriever,ImprovedRetriever
from concierge.policies import answer
from concierge.orders import lookup_order,MockOrderAPI
from concierge.handoff import create_handoff,should_escalate
class FeatureTests(unittest.TestCase):
 def test_day1_retrieval(self):self.assertTrue(Day1TfidfRetriever().search('admissions documents'))
 def test_improved_retrieval(self):self.assertTrue(ImprovedRetriever().search('refund request'))
 def test_citation_answer(self):self.assertTrue(answer('How do I request a refund?')['citations'])
 def test_abstention(self):self.assertEqual(answer('Explain quantum teleportation')['status'],'abstained')
 def test_order_success_notfound(self):self.assertEqual(lookup_order('DEMO-1001')['status'],'success');self.assertEqual(lookup_order('DEMO-404')['status'],'not_found')
 def test_order_failures(self):
  self.assertEqual(lookup_order('x',MockOrderAPI('timeout'))['status'],'timeout');self.assertEqual(lookup_order('x',MockOrderAPI('service_error'))['status'],'service_error');self.assertEqual(lookup_order('x',MockOrderAPI('malformed'))['status'],'malformed_response')
 def test_escalation_condition(self):self.assertTrue(should_escalate({'status':'abstained'}))
 def test_handoff_payload(self):
  t=create_handoff('uncertain','sample question');self.assertIn('ticket_id',t);self.assertIn('no support agent',t['notice'])
if __name__=='__main__':unittest.main()
