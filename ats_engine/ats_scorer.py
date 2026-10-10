from utils.logger import logger
from skill_extraction.skill_extractor import extract_skills


def calculate_ats_score(candidate, job, resume_text=None):
    logger.info("ATS scoring started")

    score = 0

    # Extract skills from resume text if provided
    if resume_text:
       extracted_skills = extract_skills(resume_text)
       candidate_skills_list = []
       for category_skills in extracted_skills.values():
        candidate_skills_list.extend(category_skills)
        candidate_skills = {
        skill.lower() for skill in candidate_skills_list
    }
    else:
     candidate_skills = {
        skill.lower()
        for skill in candidate.get("skills", [])
    }

    job_skills = {
        skill.lower()
        for skill in job.get("skills", [])
    }

    if job_skills:
        matched_skills = candidate_skills.intersection(job_skills)
        score += (len(matched_skills) / len(job_skills)) * 50

    # Experience score
    if candidate.get("experience"):
        score += 30

    # Education score
    if candidate.get("education"):
        score += 20

    logger.info("ATS scoring completed")
    
    return round(score, 2)
