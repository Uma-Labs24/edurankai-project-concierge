# FAILURES.md — Day 1

## Status
No results on the actual assessment corpus are claimed. The included content is fictional demo policy.

## Known design limitations (not observed corpus failures)
- TF-IDF is lexical and can miss paraphrases or synonym-heavy wording.
- Word-window chunking may separate a policy clause from its heading or exception.
- Similarity score is not calibrated confidence and is not proof of correctness.
- Source-hit evaluation does not measure generated-answer factuality or abstention quality.
- The included reference labels apply only to the demo document.

## Observed failures
After running on actual assessment documents, add concrete question IDs, expected behavior, actual retrieval, root-cause hypothesis, and fix. Do not label guesses as observed failures.

| Question ID | Expected | Actual | Cause | Fix |
|---|---|---|---|---|
| Pending actual-corpus run | — | — | — | Add corpus and evaluate |

## Metrics
Actual corpus/version: pending. Document/chunk count: pending. Hit@3 and MRR: pending.
