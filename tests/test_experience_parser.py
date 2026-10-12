from parsers.experience_parser import parse_experience


def test_parse_experience():
    resume_text = (
        "Python Developer at ABC Technologies "
        "from Jan 2021 to Dec 2023"
    )

    result = parse_experience(resume_text)

    assert "experiences" in result
    assert "total_experience_months" in result
    assert "employment_gaps" in result
    assert "overlapping_roles" in result

    assert len(result["experiences"]) == 1
    assert result["total_experience_months"] == 36

def test_employment_gap_detection():
    resume_text = """
    Python Developer at ABC Technologies
    Jan 2018 to Dec 2019

    Data Analyst at XYZ Solutions
    Jan 2021 to Dec 2022
    """

    result = parse_experience(resume_text)

    assert len(result["experiences"]) == 2
    assert len(result["employment_gaps"]) >= 1


def test_overlapping_roles_detection():
    resume_text = """
    Python Developer at ABC Technologies
    Jan 2020 to Dec 2022

    Data Analyst at XYZ Solutions
    Jan 2022 to Dec 2023
    """

    result = parse_experience(resume_text)

    assert len(result["experiences"]) == 2
    assert len(result["overlapping_roles"]) >= 1
