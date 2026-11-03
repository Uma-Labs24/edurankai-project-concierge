# Policy Change Log

| Date | Document | Version | Change | Source status |
|---|---|---:|---|---|
| 2026-11-01 | admissions_policy.md | 1.1 | Added instruction to verify eligibility and document requirements against the latest official notice. | Mock sample source; replace with approved source |
| 2026-10-15 | refund_policy.md | 1.0 | Added initial refund guidance; avoids unsupported promises. | Mock sample source |
| 2026-10-15 | order_support.md | 1.0 | Added order lookup and no-invented-status guidance. | Mock sample source |

## Update procedure
1. Save the approved policy text in `data/documents/`.
2. Update its version, source name/URL, effective date, and summary in `docs/policy_versions.json`.
3. Add a dated row above.
4. Add tests for changed rules and run `python -m unittest discover -s tests -v`.
5. Never describe sample policy text as an official institutional policy.
