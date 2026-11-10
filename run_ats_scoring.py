# Day 13 - Candidate Score Generator

from ats_engine.ats_scorer import generate_candidate_score


# Candidate Information

candidate = {
    "candidate_id": "C123",
    "skill_score": 90,
    "experience_score": 85,
    "education_score": 80,
    "semantic_score": 88
}


# Job Information

job = {
    "job_title": "Backend Developer"
}


# Generate ATS Score

result = generate_candidate_score(candidate, job)


# Display Results

print("\n========== ATS SCORING RESULTS ==========")

print("Candidate ID:", result["candidate_id"])

print("Final ATS Score:", result["final_score"], "%")

print("\nWeights Used:")

for key, value in result["weights_used"].items():
    print(key, ":", value * 100, "%")


print("\nScore Breakdown:")

for key, value in result["breakdown"].items():
    print(key, ":", value)


print("=========================================")


# Test Missing Data Handling

print("\n===== MISSING DATA TEST =====")

incomplete_candidate = {
    "candidate_id": "C124",
    "skill_score": 90,
    "experience_score": None,
    "education_score": 80,
    "semantic_score": 75
}

missing_result = generate_candidate_score(
    incomplete_candidate,
    job
)

print("Candidate ID:", missing_result["candidate_id"])
print("Final ATS Score:", missing_result["final_score"], "%")
print("Score Breakdown:", missing_result["breakdown"])
