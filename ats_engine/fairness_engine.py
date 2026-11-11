# score_normalization

def normalize_scores(candidate_scores):
    """
    Apply min-max normalization across candidates.
    """

    if not candidate_scores:
        return []

    scores = [
        float(c["final_score"])
        for c in candidate_scores
    ]

    min_score = min(scores)
    max_score = max(scores)

    for candidate in candidate_scores:

        if max_score == min_score:
            candidate["normalized_score"] = 100.0

        else:
            candidate["normalized_score"] = round(
                ((float(candidate["final_score"]) - min_score)
                 / (max_score - min_score)) * 100,
                2
            )

    return candidate_scores


#Sensitive Data Masking

def mask_sensitive_data(candidate):
    """
    Remove or mask non-essential personal attributes.
    """

    candidate = candidate.copy()

    sensitive_fields = [
        "name",
        "gender",
        "age",
        "photo",
        "location"
    ]

    for field in sensitive_fields:

        if field in candidate:
            candidate[field] = "MASKED"

    return candidate

#Keyword Bias Reduction

def reduce_keyword_bias(skill_score, semantic_score):


    """
    Reduce over-dependence on keyword matching.
    """

    adjusted_score = (
        (0.6 * semantic_score) +
        (0.4 * skill_score)
    )

    return round(adjusted_score, 2)


#Fair Candidate score generation

def generate_fair_score(candidate):
    """
    Generate bias-reduced candidate score.
    """

    skill_score = candidate.get("skill_score", 0)

    semantic_score = candidate.get(
        "semantic_score", 0
    )

    fair_score = reduce_keyword_bias(
        skill_score,
        semantic_score
    )

    candidate["fair_score"] = fair_score

    return candidate

