"""Small repeatable evaluation runner; reports counts, not fabricated scores."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from concierge.answering import answer_question
from concierge.orders import lookup_order

def main():
    cases = json.loads((ROOT / "eval" / "adversarial_questions.json").read_text(encoding="utf-8"))
    rows = []
    for case in cases:
        result = answer_question(case["question"])
        rows.append({
            "id": case["id"],
            "question": case["question"],
            "actual_status": result["status"],
            "citation_count": len(result["citations"]),
            "expected": case["expected"],
        })
    report = {
        "note": "Observed outputs from this local run; not a claim of passing or production readiness.",
        "cases": len(rows),
        "abstained": sum(row["actual_status"] == "abstained" for row in rows),
        "answered": sum(row["actual_status"] == "answered" for row in rows),
        "results": rows,
        "order_smoke_checks": {
            "success": lookup_order("ORD-1001").status,
            "not_found": lookup_order("ORD-9999").status,
        },
    }
    output = ROOT / "reports" / "latest_evaluation.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    print(f"\nSaved observed run to: {output}")

if __name__ == "__main__":
    main()
