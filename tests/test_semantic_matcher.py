from ats_engine.semantic_matcher import (
    compute_similarity,
    classify_match
)


def test_compute_similarity():
    score = compute_similarity(
        "Python machine learning",
        "Python machine learning"
    )

    assert 0 <= score <= 1
    assert score > 0.9


def test_classify_strong_match():
    assert classify_match(90) == "Strong Match"


def test_classify_moderate_match():
    assert classify_match(75) == "Moderate Match"


def test_classify_weak_match():
    assert classify_match(50) == "Weak Match"
