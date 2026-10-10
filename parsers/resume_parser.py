from utils.logger import logger
from skill_extraction.skill_extractor import extract_skills

def parse_resume(resume_text):
    logger.info("Resume parsing started")

    #extract skills from resume text
    extracted_skills=extract_skills(resume_text)

    #preapare the parsed resume result
    result = {
        "skills": extracted_skills,
        "experience":[],
        "education":[]
    }
    logger.info("Resume parsing completed")
    return result
 