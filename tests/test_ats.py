from ats_engine.ats_scorer import calculate_ats_score

def test_ats_score():
    candidate = {
        "skills" : ["Python", "SQL"],
        "experience" : ["Data Science"],
        "education" : ["MSc"]
    }
    job = {
        "skills" : ["Python", "SQL"]
    }
    score = calculate_ats_score(candidate, job)
    assert score == 100