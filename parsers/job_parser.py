import re
from utils.logger import logger


def extract_role(text):
    match = re.search(
        r"(?:JOB TITLE|ROLE|POSITION)\s*:\s*(.+)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return ""


def extract_skills(text):
    match = re.search(
        r"(?:REQUIRED SKILLS|SKILLS)\s*:?\s*(.*?)(?=\n\s*(?:EXPERIENCE|EDUCATION|RESPONSIBILITIES)\s*:?)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if not match:
        return []

    skills_text = match.group(1)

    skills = re.split(r",|\n|•|-", skills_text)

    return [
        skill.strip()
        for skill in skills
        if skill.strip()
    ]


def extract_experience(text):
    match = re.search(
        r"(?:EXPERIENCE|EXPERIENCE REQUIRED)\s*:?\s*(.*?)(?=\n\s*(?:EDUCATION|RESPONSIBILITIES)\s*:?)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return ""


def extract_education(text):
    match = re.search(
        r"(?:EDUCATION|EDUCATIONAL QUALIFICATION)\s*:?\s*(.*?)(?=\n\s*(?:RESPONSIBILITIES|REQUIREMENTS|SKILLS)\s*:?)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return ""


def parse_job_description(file_path):
    logger.info("Job description parsing started")

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    result = {
        "role": extract_role(text),
        "required_skills": extract_skills(text),
        "experience_required": extract_experience(text),
        "education_required": extract_education(text)
    }

    logger.info("Job description parsing completed")

    return result

