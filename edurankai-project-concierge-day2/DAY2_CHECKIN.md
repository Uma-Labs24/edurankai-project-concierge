# Day 2 Check-in — Project Concierge

**Status:** Day 2 starter implementation prepared for local integration and review.

## Included
- Policy version/source/effective-date metadata and a change log.
- Source-aware answers with document/version citations.
- Evidence-threshold abstention.
- Order lookup result handling for success, timeout, service error, not found,
  invalid request, and malformed payload.
- Ten adversarial evaluation questions.
- Evaluation runner and regression tests.
- README and known-failures documentation.

## Data and integration notes
- All included policy text and order records are **mock/sample data**.
- No live order API specification or credentials were supplied; no live API is claimed.
- The evaluation report is generated only when the runner is executed. No
  assessment score or pass result is invented in this check-in.

## Run locally
```bash
python -m unittest discover -s tests -v
python eval/run_evaluation.py
python -m concierge.cli
```

## Day 2 verification checklist
- [ ] Merge into the existing Day 1 repository without deleting Day 1 files.
- [ ] Run regression tests on the target machine.
- [ ] Inspect `reports/latest_evaluation.json`.
- [ ] Replace mock policy documents with approved sources and update metadata.
- [ ] Connect a real order API only after receiving its documented contract.
- [ ] Review the code with the internship mentor before claiming completion.

## Honest completion note
This is a runnable Day 2 extension scaffold, not proof of a completed internship
assessment or production-ready system. Final status depends on integration,
review, and observed test/evaluation results in the user's repository.
