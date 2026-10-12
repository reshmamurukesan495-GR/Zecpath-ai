from utils.logger import logger


def calculate_experience_relevance(candidate, job):
    """Calculate experience relevance based on job title and skills."""

    logger.info("Experience relevance scoring started")

    score = 0

    # Compare candidate job title with required job title
    candidate_title = candidate.get("job_title", "").lower()
    job_title = job.get("job_title", "").lower()

    if candidate_title and job_title:
        if candidate_title == job_title:
            score += 50
        elif candidate_title in job_title or job_title in candidate_title:
            score += 25

    # Compare candidate skills with required skills
    candidate_skills = {
        skill.lower() for skill in candidate.get("skills", [])
    }

    job_skills = {
        skill.lower() for skill in job.get("skills", [])
    }

    if job_skills:
        matched_skills = candidate_skills.intersection(job_skills)
        score += (len(matched_skills) / len(job_skills)) * 50

    logger.info("Experience relevance scoring completed")

    return round(min(score, 100), 2)
