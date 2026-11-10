# =====================================
# DAY 14 - CANDIDATE RANKING ENGINE
# =====================================

def rank_candidates(candidates):
    """
    Sort candidates in descending order
    based on their final ATS score.
    """

    ranked = sorted(
        candidates,
        key=lambda x: x.get("final_score") or 0,
        reverse=True
    )

    # Assign rank
    for idx, candidate in enumerate(ranked, start=1):
        candidate["rank"] = idx

    return ranked

# =====================================
# THRESHOLD CONFIGURATION
# =====================================

THRESHOLDS = {
    "shortlist": 75,
    "review": 50
}


# =====================================
# CANDIDATE CLASSIFICATION
# =====================================

def classify_candidate(score):

    if score >= THRESHOLDS["shortlist"]:
        return "Shortlisted"

    elif score >= THRESHOLDS["review"]:
        return "Review"

    else:
        return "Rejected"


# =====================================
# APPLY SHORTLISTING LOGIC
# =====================================

def apply_shortlisting(candidates):

    for candidate in candidates:

        score = candidate.get("final_score") or 0

        candidate["status"] = classify_candidate(score)

    return candidates


# =====================================
# TOP CANDIDATE SELECTOR
# =====================================

def get_top_candidates(candidates, top_n=5):

    shortlisted = [
        candidate for candidate in candidates
        if candidate["status"] == "Shortlisted"
    ]

    return shortlisted[:top_n]


# =====================================
# COMPLETE RANKING PIPELINE
# =====================================

def ranking_pipeline(candidates):

    ranked = rank_candidates(candidates)

    shortlisted = apply_shortlisting(ranked)

    top_candidates = get_top_candidates(shortlisted)

    return {
        "ranked_list": shortlisted,
        "top_candidates": top_candidates
    }


def generate_recruiter_report(candidates, job_id="J456"):

    result = ranking_pipeline(candidates)

    ranked = result["ranked_list"]

    summary = {
        "total_candidates": len(ranked),
        "shortlisted": sum(
            1 for c in ranked if c["status"] == "Shortlisted"
        ),
        "review": sum(
            1 for c in ranked if c["status"] == "Review"
        ),
        "rejected": sum(
            1 for c in ranked if c["status"] == "Rejected"
        )
    }

    return {
        "job_id": job_id,
        "summary": summary,
        "top_candidates": [
            {
                "candidate_id": c["candidate_id"],
                "score": c["final_score"],
                "status": c["status"]
            }
            for c in result["top_candidates"]
        ]
    }
