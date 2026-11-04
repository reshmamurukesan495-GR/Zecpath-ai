from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Load the pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Generate embeddings
def get_embedding(text):
    if not text or not text.strip():
        return np.zeros(384)

    return model.encode(text, convert_to_numpy=True)


# Calculate semantic similarity
def compute_similarity(text1, text2):
    if not text1.strip() or not text2.strip():
        return 0.0

    embedding1 = get_embedding(text1)
    embedding2 = get_embedding(text2)

    similarity = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return round(float(similarity), 4)


# Section-wise resume-to-job-description matching
def match_resume_to_jd(resume, jd):

    results = {}

    # Skills matching
    resume_skills = " ".join(
        resume.get("skills", [])
    )

    jd_skills = " ".join(
        jd.get("required_skills", [])
    )

    results["skills_similarity"] = compute_similarity(
        resume_skills,
        jd_skills
    )

    # Experience matching
    resume_exp = " ".join(
        exp.get("role", "")
        for exp in resume.get("experience", [])
    )

    jd_role = jd.get("job_title", "")

    results["experience_similarity"] = compute_similarity(
        resume_exp,
        jd_role
    )

    # Project matching
    resume_projects = " ".join(
        project.get("description", "")
        for project in resume.get("projects", [])
    )

    jd_description = jd.get("job_description_text", "")

    results["project_similarity"] = compute_similarity(
        resume_projects,
        jd_description
    )

    # Calculate the weighted final score
    final_score = (
        0.4 * results["skills_similarity"]
        + 0.3 * results["experience_similarity"]
        + 0.3 * results["project_similarity"]
    )

    results["final_similarity_score"] = round(
        final_score * 100, 2
    )

    return results


# Classify the match based on its score
def classify_match(score):

    if score >= 85:
        return "Strong Match"

    elif score >= 65:
        return "Moderate Match"

    else:
        return "Weak Match"
