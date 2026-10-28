def calculate_education_relevance(
    candidate_degree,
    required_degree,
):
    """Calculate degree relevance using simple matching rules."""

    if not candidate_degree or not required_degree:
        return 0

    candidate_degree = candidate_degree.lower().strip()
    required_degree = required_degree.lower().strip()

    if candidate_degree == required_degree:
        return 1.0

    elif (
        candidate_degree in ["m.tech", "mba"]
        and required_degree in ["b.tech", "b.e"]
    ):
        return 0.8

    else:
        return 0.5


def calculate_certification_relevance(certifications, job_skills):
    """Calculate certification relevance against job skills."""

    score = 0

    job_skills = [
        skill.lower().strip()
        for skill in job_skills
    ]

    for cert in certifications:

        category = cert["category"].lower()

        if category in job_skills:
            score += 1

    if len(certifications) == 0:
        return 0

    return round(
        (score / len(certifications)) * 100,
        2,
    )
