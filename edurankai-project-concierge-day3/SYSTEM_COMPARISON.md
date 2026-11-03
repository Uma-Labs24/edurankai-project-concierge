# System comparison
Day 1 = TF-IDF cosine baseline. Improved = TF-IDF plus title and phrase boosts. `eval/compare_systems.py` computes Recall@3 on bundled labelled demo questions, citation coverage (unavailable for citation-less baseline), abstention count, and retrieval latency. Results are emitted in `reports/system_comparison.json`; small synthetic dataset is not a broad quality guarantee.
