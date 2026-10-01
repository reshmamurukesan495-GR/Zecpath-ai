from utils.logger import logger

def calculate_ats_score(candidate, job):
    logger.info("ATS scoring started")

    score=0

    if candidate.get("skills"):
        score +=50
    if candidate.get("experience"):
        score +=30
    if candidate.get("education"):
        score +=20
    logger.info("ATS scoring completed")
    return score