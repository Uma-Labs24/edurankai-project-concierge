# EduRankAI Project Concierge

Document-grounded support assistant: retrieve relevant source passages and avoid unsupported answers.

**Day 1 baseline only.** Included policy and questions are fictional demo content. Replace with the assessment's actual corpus before reporting results. This is not the completed 3-day submission yet.

## Three-day repository plan
- Day 1: audit documents, chunking/retrieval baseline, 40+ evaluation questions, metrics and failure analysis.
- Day 2: incorporate policy updates, citations, abstention, resilient order lookup, adversarial tests.
- Day 3: latency/cost measurements, compare two approaches, human handoff, regression tests, decision memo.

## Setup
Python 3.10+ recommended.

```bash
python -m venv .venv
```
Windows CMD: `.venv\\Scripts\\activate`
PowerShell: `.venv\\Scripts\\Activate.ps1`
macOS/Linux: `source .venv/bin/activate`

```bash
python -m pip install -r requirements.txt
```

Put real `.txt` or `.md` documents into `data/documents/`. Then:

```bash
python -m concierge.build_index
python -m concierge.search "How long does a customer have to request a refund?"
python -m concierge.evaluate
python -m unittest discover -s tests
```

Evaluation output: `reports/day1_baseline.json`. It measures retrieval source-hit proxy, not final answer correctness. Only report metrics after running on the real corpus and verifying reference labels.

## Structure
- `concierge/`: chunking, TF-IDF retrieval, index builder, CLI search, evaluator
- `data/documents/`: corpus directory
- `data/demo/`: fictional example policy
- `eval/`: 40-question demo evaluation set
- `FAILURES.md`: honest failure log
- `DAY1_CHECKIN.md`: daily check-in draft

## Git
```bash
git init
git add .
git commit -m "Day 1: add retrieval baseline and evaluation"
```
Continue Day 2 and Day 3 in this same repo using meaningful commits.
