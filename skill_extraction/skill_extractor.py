SKILL_DICTIONARY = {
    "technical": [
        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Power BI",
        "Pandas",
        "NumPy",
        "TensorFlow",
        "PyTorch",
        "Java",
        "JavaScript",
        "React",
        "Node.js",
        "MySQL",
        "Natural Language Processing"
    ],

    "business": [
        "Project Management",
        "Business Analysis",
        "Communication",
        "Leadership",
        "Team Management",
        "Problem Solving"
    ],

    "creative": [
        "Graphic Design",
        "UI/UX Design",
        "Content Writing",
        "Video Editing",
        "Photography"
    ]
}

SKILL_SYNONYMS = {
    "Machine Learning": ["ML"],
    "Deep Learning": ["DL"],
    "Natural Language Processing": ["NLP"],
    "JavaScript": ["JS"],
    "React": ["React.js"],
    "Node.js": ["Node"],
    "Microsoft Excel": ["Excel"],
    "Power BI": ["PowerBI"]
}

def extract_skills(resume_text):
    """
    Extract skills from resume text.
    """

    extracted_skills = {
        "technical": [],
        "business": [],
        "creative": []
    }

    resume_text_lower = resume_text.lower()

    #check normal skill names

    for category, skills in SKILL_DICTIONARY.items():
        for skill in skills:
            if skill.lower() in resume_text_lower:
                extracted_skills[category].append(skill)

    #check synonyms

    for skill, synonyms in SKILL_SYNONYMS.items():

        #find which category contains the original skill
        for category, skills in SKILL_DICTIONARY.items():
            if skill in skills:
                #check each synonym
                for synonym in synonyms:
                    if synonym.lower() in resume_text_lower:
                       extracted_skills[category].append(skill)
    #remove duplicate skills
    for category in extracted_skills:
        extracted_skills[category] = list(
            dict.fromkeys(extracted_skills[category])
        )


    return extracted_skills

def calculate_skill_confidence(resume_text,skill):
    """ 
    Calculate confidence score for a skill using its name and synonyms.
    """
    resume_text_lower = resume_text.lower()
    #check the exact skill name
    if skill.lower() in resume_text_lower:
        return 1.0
    #check whether any synonyms appears in the resume
    synonyms = SKILL_SYNONYMS.get(skill,[])
    for synonym in synonyms:
        if synonym.lower() in resume_text_lower:
            return 1.0
    

    return 0.0


def extract_skills_with_confidence(resume_text):
    """
    Extract skills and return each skill with its confidence score.
    """
    extracted_skills = extract_skills(resume_text)

    structured_output = {}

    for category, skills in extracted_skills.items():
        structured_output[category] = []

        for skill in skills:
            confidence = calculate_skill_confidence(
                resume_text, skill
            )

            structured_output[category].append({
                "skill": skill,
                "confidence": confidence
            })

    return structured_output
