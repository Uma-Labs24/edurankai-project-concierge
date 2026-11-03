import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from concierge.answering import answer_question

class AnsweringTests(unittest.TestCase):
    def test_relevant_question_has_citation(self):
        result = answer_question("What is the admissions policy for applicants and documents?")
        self.assertEqual(result["status"], "answered")
        self.assertTrue(result["citations"])
        self.assertIn("version", result["citations"][0])

    def test_unknown_detail_abstains(self):
        result = answer_question("What is the exact refund processing time?")
        self.assertEqual(result["status"], "abstained")
        self.assertEqual(result["citations"], [])

    def test_empty_evidence_abstains(self):
        result = answer_question("Explain quantum teleportation", documents=[])
        self.assertEqual(result["status"], "abstained")

if __name__ == "__main__":
    unittest.main()
