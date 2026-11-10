from ats_engine.ats_scorer import calculate_ats_score


def test_ats_score():

    candidate = {
        "skill_score": 100,
        "experience_score": 100,
        "education_score": 100,
        "semantic_score": 100
    }

    job = {
        "job_title": "Backend Developer"
    }

    score = calculate_ats_score(candidate, job)

    assert score == 100