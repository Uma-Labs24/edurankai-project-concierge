"""Order lookup adapter with explicit, testable error handling.

The included records are MOCK DATA only. Replace MockOrderAPI with a real
adapter only after an approved API specification and credentials are supplied.
"""
from dataclasses import dataclass
from typing import Optional

MOCK_ORDERS = {
    "ORD-1001": {"order_id": "ORD-1001", "status": "shipped", "eta": "2026-11-06"},
    "ORD-1002": {"order_id": "ORD-1002", "status": "processing", "eta": "2026-11-08"},
}

@dataclass
class OrderResult:
    status: str
    message: str
    order: Optional[dict] = None

class MockOrderAPI:
    """Deterministic mock service. Modes simulate common API outcomes."""
    def __init__(self, mode="success"):
        self.mode = mode

    def get_order(self, order_id):
        if self.mode == "timeout":
            raise TimeoutError("Mock timeout")
        if self.mode == "service_error":
            raise RuntimeError("Mock service unavailable")
        if self.mode == "malformed":
            return {"unexpected": "payload"}
        return MOCK_ORDERS.get(order_id)

def lookup_order(order_id, api=None):
    api = api or MockOrderAPI()
    if not isinstance(order_id, str) or not order_id.strip():
        return OrderResult("invalid_request", "Please provide a valid order ID.")
    try:
        payload = api.get_order(order_id.strip().upper())
    except TimeoutError:
        return OrderResult("timeout", "The order service timed out. Please try again later.")
    except Exception:
        return OrderResult("service_error", "The order service is temporarily unavailable.")
    if payload is None:
        return OrderResult("not_found", "No order was found for that ID.")
    if not isinstance(payload, dict) or not all(k in payload for k in ("order_id", "status", "eta")):
        return OrderResult("malformed_response", "The order service returned an invalid response.")
    if not all(isinstance(payload[k], str) for k in ("order_id", "status", "eta")):
        return OrderResult("malformed_response", "The order service returned an invalid response.")
    return OrderResult("success", "Order details retrieved.", payload)
