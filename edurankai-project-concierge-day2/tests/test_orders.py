import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from concierge.orders import lookup_order, MockOrderAPI

class OrderTests(unittest.TestCase):
    def test_success(self):
        self.assertEqual(lookup_order("ORD-1001").status, "success")

    def test_not_found(self):
        self.assertEqual(lookup_order("ORD-404").status, "not_found")

    def test_timeout(self):
        self.assertEqual(lookup_order("ORD-1001", MockOrderAPI("timeout")).status, "timeout")

    def test_service_error(self):
        self.assertEqual(lookup_order("ORD-1001", MockOrderAPI("service_error")).status, "service_error")

    def test_malformed_response(self):
        self.assertEqual(lookup_order("ORD-1001", MockOrderAPI("malformed")).status, "malformed_response")

    def test_invalid_id(self):
        self.assertEqual(lookup_order("").status, "invalid_request")

if __name__ == "__main__":
    unittest.main()
