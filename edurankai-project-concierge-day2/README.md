# EduRankAI — Project Concierge (Day 2 extension)

This folder is an **overlay extension** for the existing `edurankai-project-concierge`
Day 1 repository. It does not contain or replace your Day 1 work. Copy/merge these
files into the existing repository and resolve any same-name conflicts manually.

## Day 2 scope
- Policy documents carry version, source, and effective-date metadata.
- `docs/POLICY_CHANGELOG.md` records policy changes.
- Answers include source/version citations when evidence is adequate.
- The answer layer abstains when retrieved evidence is too weak.
- Order lookup handles success, timeout, service error, not-found, invalid ID,
  and malformed responses.
- Ten adversarial questions and a repeatable evaluation runner are included.
- Regression tests cover retrieval/abstention and order outcomes.

## Important limitations
- Policy documents and order records in this package are **MOCK / SAMPLE DATA**.
  They are not official EduRankAI or institutional policies and do not represent
  real customer orders.
- No real order API specification or credentials were supplied. `MockOrderAPI`
  is a local simulation, not a live integration.
- Retrieval uses simple keyword overlap, not a production-grade semantic model.
- No actual assessment result is claimed. Run the evaluation locally and inspect
  `reports/latest_evaluation.json`.
- This Day 2 package is a starter extension; review and adapt it to your Day 1
  interfaces before merging.

## Requirements
- Python 3.10+
- No third-party packages required (Python standard library only).

## Run
From the repository root:

```bash
python -m concierge.cli
```

Choose `1` to ask a policy question, or `2` to try mock order `ORD-1001`.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Run evaluation
```bash
python eval/run_evaluation.py
```

The runner writes observed results to `reports/latest_evaluation.json`. It does
not label the results as a pass or claim completion.

## Update a policy safely
1. Replace or add the approved document in `data/documents/`.
2. Update the matching entry in `docs/policy_versions.json`.
3. Add a row to `docs/POLICY_CHANGELOG.md`.
4. Add/adjust regression tests.
5. Run tests and evaluation; review the output.

## Day 1 merge safety
Do not delete your Day 1 repository or overwrite unrelated files. Extract this ZIP
to a separate folder, then copy the listed Day 2 folders/files into your existing
repository. If a filename already exists, compare it first and merge manually.
Commit the merged work on a new branch so Day 1 remains recoverable.
