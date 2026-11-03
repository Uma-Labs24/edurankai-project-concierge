# FAILURES.md — known gaps and failure handling

This file records known limitations honestly. It is not a claim that every case
has been solved.

## Implemented defensive handling
- Order ID missing/blank: `invalid_request`.
- Order service timeout: `timeout`.
- Other service exception: `service_error` (message hides internal exception details).
- Unknown order: `not_found`.
- Unexpected/missing/wrong-type payload fields: `malformed_response`.
- Weak or absent document evidence: `abstained`, with no citation.

## Known limitations / risks
1. **Mock data only:** order records are hard-coded examples. No live order API
   was provided or connected.
2. **Sample policies only:** policy documents are illustrative. Replace them with
   approved, dated institutional documents before relying on answers.
3. **Keyword retrieval:** word overlap can miss synonyms, context, negation, and
   nuanced questions. It can also retrieve a superficially similar document.
4. **Simple abstention threshold:** the two-term overlap threshold is a teaching
   heuristic, not a calibrated confidence score.
5. **Citation granularity:** citations identify the document and version, not
   page/paragraph offsets. Add section-level references for production use.
6. **No authentication/authorization:** do not expose real student or order data
   through this demo.
7. **No live monitoring/retries:** timeout and service failures are surfaced to
   the caller; retry/backoff and observability are not implemented.
8. **Adversarial set is a starter set:** ten fixed questions do not establish
   safety, fairness, or broad reliability.

## Follow-up work
- Obtain the actual API contract, authentication method, and approved test endpoint.
- Add document-level approval metadata and automated stale-policy checks.
- Improve retrieval and evaluate it against a reviewed, labelled question set.
- Add privacy controls, access checks, structured logs, and human escalation.
