from skill_extraction.skill_extractor import (
    extract_skills,
    extract_skills_with_confidence
)


def test_skill_extraction():
    resume = "Experienced in Python, SQL and Machine Learning"

    result = extract_skills(resume)

    assert "Python" in result["technical"]
    assert "SQL" in result["technical"]
    assert "Machine Learning" in result["technical"]


def test_skill_synonyms():
    resume = "Experienced in ML and NLP"

    result = extract_skills(resume)

    assert "Machine Learning" in result["technical"]
    assert "Natural Language Processing" in result["technical"]


def test_skill_confidence():
    resume = "Experienced in Python"

    result = extract_skills_with_confidence(resume)

    assert {
        "skill": "Python",
        "confidence": 1.0
    } in result["technical"]