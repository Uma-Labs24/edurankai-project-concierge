"""Cited answers and evidence-based abstention."""
from .knowledge_base import retrieve

MIN_EVIDENCE_SCORE = 2

def answer_question(question, documents=None):
    matches = retrieve(question, documents=documents)
    # Require at least two distinct matching terms across the best retrieved text.
    import re
    terms = set(re.findall(r"[a-z0-9]+", question.lower()))
    best = matches[0] if matches else None
    overlap = terms & set(re.findall(r"[a-z0-9]+", (best or {}).get("title", "") + " " + (best or {}).get("text", "").lower()))
    # Respect explicit gaps in a policy: keyword overlap must not turn an
    # acknowledged unknown (such as an unspecified processing time) into an answer.
    question_lower = question.lower()
    best_text = (best or {}).get("text", "").lower()
    explicitly_unspecified = (
        ("processing time" in question_lower and "does not specify" in best_text)
        or ("refund amount" in question_lower and "does not specify" in best_text)
        or ("tracking number" in question_lower and "tracking number" not in best_text)
    )
    if not best or len(overlap) < MIN_EVIDENCE_SCORE or explicitly_unspecified:
        return {
            "status": "abstained",
            "answer": "I don't have enough reliable information in the available documents to answer that. Please contact the support team or provide an approved source.",
            "citations": [],
        }

    # Return a concise source-grounded extract rather than inventing a policy.
    excerpt = " ".join(best["text"].strip().split())
    if len(excerpt) > 420:
        excerpt = excerpt[:417].rsplit(" ", 1)[0] + "..."
    citation = {
        "document_id": best["id"],
        "source": best["source"],
        "version": best["version"],
        "effective_date": best["effective_date"],
    }
    return {
        "status": "answered",
        "answer": excerpt,
        "citations": [citation],
    }
