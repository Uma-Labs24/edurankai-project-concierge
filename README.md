# edurankai-project-concierge

**A Source-Aware Support Assistant for Reliable Document-Based Answers**

Project Concierge is a document-grounded support assistant designed to help users find accurate information from a collection of support documents and policies. It retrieves relevant source passages, supports source-based responses, and is designed to avoid unsupported answers when the available information is insufficient.

The goal is to make support information easier to find while reducing incorrect or invented responses.

> **Project status:** Day 1 retrieval baseline. Day 2 and Day 3 features will be added as the project progresses. The included policy file is fictional demo content and must not be treated as real company policy.

---

## Project Objectives

- Organize and search information from support documents.
- Retrieve relevant passages for user questions.
- Keep answers grounded in the available source documents.
- Identify missing, conflicting, outdated, or unsupported information.
- Evaluate retrieval quality using a realistic question set.
- Handle service errors and unsupported questions safely.
- Improve performance while considering latency and cost.
- Provide a human handoff option when automated support is insufficient.

---

## Three-Day Development Plan

### Day 1 — Document Audit and Retrieval Baseline

- Inspect the document corpus for contradictions, outdated information, duplicates, and missing details.
- Create searchable text chunks using a transparent chunking strategy.
- Implement a TF-IDF retrieval baseline.
- Prepare an evaluation set containing 40+ realistic questions.
- Evaluate retrieval performance and inspect failure cases.
- Record limitations and risks in `FAILURES.md`.

### Day 2 — Policy Updates and Reliable Support

- Incorporate policy updates without rebuilding the entire system unnecessarily.
- Return answers with relevant source information.
- Handle unsupported questions through abstention rather than guessing.
- Integrate an order lookup service with timeout, error, and malformed-response handling.
- Test adversarial and misleading questions.
- Run an updated evaluation and document observed failures.

### Day 3 — Performance, Handoff, and Final Evaluation

- Measure latency and cost under the stated constraints.
- Compare two implementation approaches using recorded measurements.
- Add a human handoff path for unresolved or unsupported requests.
- Run regression tests against the evaluation set.
- Prepare a decision memo explaining the final approach, trade-offs, and limitations.
- Update the final report and project documentation.

---

## Current Day 1 Implementation

The initial baseline uses:

- **Python** for implementation
- **TF-IDF** for lexical retrieval
- **Cosine similarity** for ranking relevant document chunks
- **Overlapping word-window chunking** for document preparation
- **JSON** for the evaluation dataset and result reports

The retrieval baseline is intentionally simple and explainable. It provides a reference point for evaluating later improvements.

### Evaluation

The evaluation script reports:

- Number of documents
- Number of chunks
- Number of evaluation questions
- Hit Rate at 3
- Mean Reciprocal Rank (MRR)
- Retrieved source information for each question

These are retrieval-level metrics. They do not independently prove that a generated answer is factually correct.

---

## Repository Structure

```text
edurankai-project-concierge/
├── concierge/
│   ├── __init__.py
│   ├── chunking.py
│   ├── retrieval.py
│   ├── build_index.py
│   ├── search.py
│   └── evaluate.py
├── data/
│   ├── documents/
│   └── demo/
├── eval/
│   └── day1_questions.json
├── reports/
├── tests/
│   └── test_chunking.py
├── FAILURES.md
├── DAY1_CHECKIN.md
├── requirements.txt
└── README.md
```

Additional Day 2 and Day 3 files will be added to this same repository.

---

## Installation and Setup

### Requirements

- Python 3.10 or later
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Uma-Labs24/project-concierge-ai-assessment.git
cd project-concierge-ai-assessment
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows CMD**
```bat
.venv\Scripts\activate
```

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Run the Day 1 Baseline

Add the assessment's actual `.txt` or `.md` documents to:

```text
data/documents/
```

Build the searchable chunk data:

```bash
python -m concierge.build_index
```

Search the document collection:

```bash
python -m concierge.search "How long does a customer have to request a refund?"
```

Run the evaluation:

```bash
python -m concierge.evaluate
```

The evaluation report is written to:

```text
reports/day1_baseline.json
```

Run the unit tests:

```bash
python -m unittest discover -s tests
```

---

## Failure Analysis

`FAILURES.md` records:

- Expected behavior
- Actual retrieval result
- Failure cause or hypothesis
- Planned improvement
- Evaluation limitations

Only observed failures should be reported as actual failures. Potential limitations should be clearly labeled as design-level risks until they are tested.

---

## Daily Check-ins

The repository includes a Day 1 check-in draft. Daily check-ins should summarize:

- What was built
- What was tested
- What worked
- What failed
- What was learned
- Next steps
- Current blockers

Check-in notes and evaluation results must reflect the work actually completed.

---

## Limitations and Responsible Reporting

- TF-IDF is a lexical retrieval method and may miss questions phrased differently from the source.
- Word-based chunking may separate a statement from its heading or exception.
- Similarity scores are not calibrated confidence values.
- Retrieval metrics do not measure final answer factuality.
- Results depend on the quality and correctness of the source documents and evaluation labels.
- The demo policy is fictional and is included only to demonstrate the initial code structure.

No performance result should be reported as an assessment-corpus result until the actual corpus has been processed and the evaluation has been run.

---

## Git Commit History

Development will continue in one repository with meaningful commits, for example:

```text
Day 1: add document retrieval baseline and evaluation
Day 2: add policy updates and resilient support lookup
Day 3: add performance evaluation and human handoff
```

Commit messages should describe the work actually completed.

---

## Final Deliverables

The final project is expected to include:

- A GitHub repository that runs from a clean checkout
- Source code and setup instructions
- Evaluation dataset and results
- `FAILURES.md`
- Three daily check-in notes
- A report of up to four pages
- A 5–8 minute project walkthrough
- A final explanation of design decisions, trade-offs, limitations, and next steps

---

## Author

**EduRankAI Internship Challenge — Project Concierge**

Built as a three-day project focused on document-grounded retrieval, reliable support responses, and evaluation.
