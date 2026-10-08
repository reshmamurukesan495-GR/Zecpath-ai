import re


SECTION_PATTERNS = {
    "skills": [
        r"^skills?$",
        r"^technical skills$",
        r"^core skills$",
        r"^key skills$"
    ],
    "work_experience": [
        r"^experience$",
        r"^work experience$",
        r"^professional experience$",
        r"^employment history$"
    ],
    "education": [
        r"^education$",
        r"^educational background$",
        r"^academic background$"
    ],
    "certifications": [
        r"^certifications?$",
        r"^professional certifications$",
        r"^certificates$"
    ],
    "projects": [
        r"^projects?$",
        r"^academic projects$",
        r"^personal projects$"
    ]
}


def classify_section_heading(heading):
    """Classify a resume heading into a known section."""

    heading = heading.strip().lower()

    for section, patterns in SECTION_PATTERNS.items():
        for pattern in patterns:
            if re.match(pattern, heading):
                return section

    return "unknown"