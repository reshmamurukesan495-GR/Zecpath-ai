from scoring.experience_scorer import calculate_experience_relevance


def test_experience_relevance():
    candidate = {
        "job_title": "Python Developer",
        "skills": ["Python", "SQL", "Machine Learning"]
    }

    job = {
        "job_title": "Python Developer",
        "skills": ["Python", "SQL"]
    }

    score = calculate_experience_relevance(candidate, job)

    assert score == 100