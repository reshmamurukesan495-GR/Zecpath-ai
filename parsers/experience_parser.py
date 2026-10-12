import re
from datetime import datetime

from utils.logger import logger


def parse_experience(resume_text):
    """Extract work experience information from resume text."""

    logger.info("Experience parsing started")

    experience = []

    date_pattern = (
        r"\b("
        r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
        r"[a-z]*\s+\d{4}|\d{4}"
        r")\s*(?:to|-|–|—)\s*("
        r"Present|Current|"
        r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
        r"[a-z]*\s+\d{4}|\d{4}"
        r")\b"
    )

    def parse_date(date_text):
        """Convert a date string into a datetime object."""

        date_text = date_text.strip()

        date_formats = [
            "%b %Y",
            "%B %Y",
            "%Y",
        ]

        for date_format in date_formats:
            try:
                parsed = datetime.strptime(date_text, date_format)

                if date_format == "%Y":
                    parsed = parsed.replace(month=1, day=1)

                return parsed

            except ValueError:
                continue

        return None

    def calculate_duration(start_date, end_date):
        """Calculate employment duration in months."""

        start = parse_date(start_date)

        if end_date.lower() in ["present", "current"]:
            end = datetime.today()
        else:
            end = parse_date(end_date)

        if start is None or end is None or end < start:
            return None

        return (
            (end.year - start.year) * 12
            + end.month - start.month
            + 1
        )

    # Find employment date ranges.
    date_matches = re.findall(
        date_pattern,
        resume_text,
        flags=re.IGNORECASE,
    )

    # Extract a company and job title when possible.
    lines = resume_text.splitlines()

    for start_date, end_date in date_matches:
        duration = calculate_duration(start_date, end_date)

        if duration is None:
            continue

        # Search for the date range in the resume.
        matching_index = None

        for index, line in enumerate(lines):
            if (
                start_date.lower() in line.lower()
                and end_date.lower() in line.lower()
            ):
                matching_index = index
                break

        job_title = None
        company = None

        # Use the preceding lines as possible job details.
        if matching_index is not None:
            if matching_index >= 1:
                job_title = lines[matching_index - 1].strip() or None

            if matching_index >= 2:
                company = lines[matching_index - 2].strip() or None

        experience.append({
            "company": company,
            "job_title": job_title,
            "start_date": start_date,
            "end_date": end_date,
            "duration_months": duration,
        })

    # Calculate total experience.
    total_experience_months = sum(
        item["duration_months"] for item in experience
    )

    # Sort roles by start date.
    def sort_key(item):
        date = parse_date(item["start_date"])
        return date if date else datetime.max

    sorted_experience = sorted(experience, key=sort_key)

    employment_gaps = []
    overlapping_roles = []

    # Detect gaps and overlapping employment periods.
    for index in range(1, len(sorted_experience)):
        previous = sorted_experience[index - 1]
        current = sorted_experience[index]

        previous_end = (
            datetime.today()
            if previous["end_date"].lower() in ["present", "current"]
            else parse_date(previous["end_date"])
        )

        current_start = parse_date(current["start_date"])

        if previous_end is None or current_start is None:
            continue

        if current_start > previous_end:
            gap_months = (
                (current_start.year - previous_end.year) * 12
                + current_start.month - previous_end.month
                - 1
            )

            if gap_months > 0:
                employment_gaps.append({
                    "from": previous["end_date"],
                    "to": current["start_date"],
                    "gap_months": gap_months,
                })

        elif current_start <= previous_end:
            overlapping_roles.append({
                "previous_role": previous["job_title"],
                "current_role": current["job_title"],
            })

    logger.info("Experience parsing completed")

    return {
        "experiences": experience,
        "total_experience_months": total_experience_months,
        "employment_gaps": employment_gaps,
        "overlapping_roles": overlapping_roles,
    }
