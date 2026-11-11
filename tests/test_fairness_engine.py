from ats_engine.fairness_engine import (
    normalize_scores,
    mask_sensitive_data,
    reduce_keyword_bias,
    generate_fair_score
)


def test_normalization():

    candidates = [
        {"final_score": 50},
        {"final_score": 100}
    ]

    result = normalize_scores(candidates)

    assert result[0]["normalized_score"] == 0
    assert result[1]["normalized_score"] == 100


def test_mask_sensitive_data():

    candidate = {
        "candidate_id": "C1",
        "name": "John",
        "gender": "Male",
        "age": 25,
        "location": "Kerala"
    }

    result = mask_sensitive_data(candidate)

    assert result["name"] == "MASKED"
    assert result["gender"] == "MASKED"
    assert result["age"] == "MASKED"
    assert result["location"] == "MASKED"


def test_keyword_bias_reduction():

    result = reduce_keyword_bias(80, 90)

    assert result == 86


def test_fair_score():

    candidate = {
        "candidate_id": "C1",
        "skill_score": 80,
        "semantic_score": 90
    }

    result = generate_fair_score(candidate)

    assert result["fair_score"] == 86


def test_empty_candidates():

    result = normalize_scores([])

    assert result == []
