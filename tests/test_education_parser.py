from parsers.education_parser import (
    extract_education,
    extract_certifications,
)


def test_education():
    text = "B.Tech in Computer Science from XYZ University (2021)"

    result = extract_education(text)

    assert len(result) > 0
    assert result[0]["degree"] == "B.Tech"
    assert result[0]["field"] == "Computer Science"
    assert result[0]["year_of_completion"] == "2021"


def test_certifications():
    text = "AWS Certified Developer and Machine Learning Course"

    result = extract_certifications(text)

    assert len(result) == 2

    names = [item["name"] for item in result]

    assert "Aws" in names
    assert "Machine Learning" in names
