from ats_engine.semantic_matcher import (
    match_resume_to_jd,
    classify_match
)

# Sample resume
resume = {
    "skills": ["Python", "Django", "REST API"],
    "experience": [
        {"role": "Backend Developer"}
    ],
    "projects": [
        {
            "description": "Built scalable REST APIs using Django"
        }
    ]
}

# Sample job description
jd = {
    "job_title": "Backend Developer",
    "required_skills": ["Python", "Django", "API"],
    "job_description_text": (
        "Looking for a backend developer "
        "to build APIs and scalable systems"
    )
}

# Calculate similarity
result = match_resume_to_jd(resume, jd)

# Classify the match
match_type = classify_match(
    result["final_similarity_score"]
)

print("Semantic Matching Results")
print("-------------------------")
print("Skills Similarity:", result["skills_similarity"])
print("Experience Similarity:", result["experience_similarity"])
print("Project Similarity:", result["project_similarity"])
print("Final Score:", result["final_similarity_score"])
print("Match Type:", match_type)
