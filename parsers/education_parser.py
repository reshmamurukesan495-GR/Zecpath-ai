import re

from utils.logger import logger


# 1. Degree Mapping


DEGREE_MAP = {
    "btech": "B.Tech",
    "b.tech": "B.Tech",
    "b.e": "B.Tech",
    "be": "B.Tech",
    "mtech": "M.Tech",
    "m.tech": "M.Tech",
    "m.e": "M.Tech",
    "mba": "MBA",
    "bsc": "B.Sc",
    "b.sc": "B.Sc",
    "msc": "M.Sc",
    "m.sc": "M.Sc",
    "bca": "BCA",
    "mca": "MCA",
    "phd": "PhD",
}


# 2. Certification Categories

CERT_CATEGORIES = {
    "aws": "Cloud",
    "azure": "Cloud",
    "gcp": "Cloud",
    "python": "Programming",
    "data science": "Data",
    "machine learning": "AI",
    "scrum": "Management",
}


# 3. Normalize Text

def clean_text(text):
    """Convert text into a normalized format."""

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s.,()\-]", "", text)

    return text


# 4. Extract Education

def extract_education(text):
    """Extract degree, field, institution and completion year."""

    text = clean_text(text)

    education_list = []

    for key, value in DEGREE_MAP.items():

        pattern = (
            r"(?<![a-z0-9])"
            + re.escape(key)
            + r"(?![a-z0-9])"
        )

        if not re.search(pattern, text):
            continue

        # Extract a four-digit year.
        year_match = re.search(r"\b(19\d{2}|20\d{2})\b", text)

        year = year_match.group(1) if year_match else None

        # Extract field of study.
        field = "Not Specified"

        field_match = re.search(
            r"\bin\s+([a-z][a-z ]*?)"
            r"\s+(?:from|at)\b",
            text,
        )

        if field_match:
            field = field_match.group(1).strip().title()

        # Extract institution.
        institution = "Not Extracted"

        institution_match = re.search(
            r"\b(?:from|at)\s+"
            r"([a-z][a-z0-9 .&-]*?)"
            r"\s*(?:\(\s*(?:19|20)\d{2}\s*\)|"
            r"\b(?:19|20)\d{2}\b|$)",
            text,
        )

        if institution_match:
            institution = institution_match.group(1).strip().title()

        education_list.append({
            "degree": value,
            "field": field,
            "institution": institution,
            "year_of_completion": year,
        })

        # Stop after finding the first matching degree.
        break

    return education_list


# 5. Extract Certifications

def extract_certifications(text):
    """Extract certification keywords and categorize them."""

    text = clean_text(text)

    certifications = []

    for keyword, category in CERT_CATEGORIES.items():

        if re.search(
            r"(?<![a-z0-9])"
            + re.escape(keyword)
            + r"(?![a-z0-9])",
            text,
        ):

            certifications.append({
                "name": keyword.title(),
                "category": category,
            })

    return certifications
