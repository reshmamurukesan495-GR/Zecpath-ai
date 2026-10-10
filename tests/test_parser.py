from parsers.resume_parser import parse_resume


def test_resume_parser_extracts_skills():
    resume_text = "Experienced in Python, SQL and Machine Learning"

    result = parse_resume(resume_text)

    assert "skills" in result
    assert "experience" in result
    assert "education" in result

    assert "Python" in result["skills"]["technical"]
    assert "SQL" in result["skills"]["technical"]
    assert "Machine Learning" in result["skills"]["technical"]
