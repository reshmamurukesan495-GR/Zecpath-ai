from ats_engine.ranking_engine import generate_recruiter_report

# Sample candidate data
candidates = [
    {"candidate_id": "C1", "final_score": 88},
    {"candidate_id": "C2", "final_score": 72},
    {"candidate_id": "C3", "final_score": 45},
    {"candidate_id": "C4", "final_score": 80}
]

# Generate recruiter report
report = generate_recruiter_report(candidates)

# Display output
print("\n===== RECRUITER REPORT =====")

print("Job ID:", report["job_id"])

print("\nSummary:")

for key, value in report["summary"].items():
    print(key, ":", value)

print("\nTop Candidates:")

for candidate in report["top_candidates"]:
    print(candidate)
