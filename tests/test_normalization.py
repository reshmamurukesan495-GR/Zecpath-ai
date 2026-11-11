from parsers.normalization import normalize_resume_text


def test_lowercase():
    result = normalize_resume_text("PYTHON DEVELOPER")
    assert result == "python developer"


def test_heading_replacement():
    result = normalize_resume_text("Professional Experience")
    assert result == "experience"


def test_space_normalization():
    result = normalize_resume_text("Python     SQL")
    assert result == "python sql"


def test_special_characters():
    result = normalize_resume_text("Python: Developer!")
    assert result == "python developer"
