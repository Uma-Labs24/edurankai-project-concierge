# Project Concierge Day 3
Fictional demo corpus only: no real EduRankAI internal documents/customer data. Python 3.10+, standard library only.

Windows CMD from project root:
```bat
python --version
python -m venv .venv
.venv\Scripts\activate
python -m unittest discover -s tests -v
python eval\compare_systems.py
python eval\benchmark.py
python -m concierge.cli
```
Benchmark measures retrieval and local extractive pipeline average/median/p95. Cost uses clearly stated illustrative token/rate assumptions; no API is called and actual cost is null. Handoff appends local JSONL only; no agent contacted. Merge into the existing Day 1/2 repo carefully, compare collisions, do not delete old files.

Structure: `concierge/` source; `data/documents/` demo policies; `docs/` version metadata; `eval/` benchmark/comparison/questions; `reports/` outputs; `tests/` regression suite.
