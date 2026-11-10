from ats_engine.ranking_engine import (
    rank_candidates,
    ranking_pipeline,
    generate_recruiter_report
)


def test_ranking():

    candidates = [
        {"candidate_id": "C1", "final_score": 50},
        {"candidate_id": "C2", "final_score": 80}
    ]

    ranked = rank_candidates(candidates)

    assert ranked[0]["candidate_id"] == "C2"


def test_shortlisting():

    candidates = [
        {"candidate_id": "C1", "final_score": 88},
        {"candidate_id": "C2", "final_score": 72},
        {"candidate_id": "C3", "final_score": 45},
        {"candidate_id": "C4", "final_score": 80}
    ]

    result = ranking_pipeline(candidates)

    ranked = result["ranked_list"]

    assert ranked[0]["candidate_id"] == "C1"
    assert ranked[0]["status"] == "Shortlisted"

    assert ranked[1]["candidate_id"] == "C4"
    assert ranked[1]["status"] == "Shortlisted"

    assert ranked[2]["status"] == "Review"
    assert ranked[3]["status"] == "Rejected"

    assert len(result["top_candidates"]) == 2

def test_recruiter_report():

    candidates = [
        {"candidate_id": "C1", "final_score": 88},
        {"candidate_id": "C2", "final_score": 72},
        {"candidate_id": "C3", "final_score": 45},
        {"candidate_id": "C4", "final_score": 80}
    ]

    report = generate_recruiter_report(candidates)

    assert report["job_id"] == "J456"

    assert report["summary"]["total_candidates"] == 4

    assert report["summary"]["shortlisted"] == 2

    assert report["summary"]["review"] == 1

    assert report["summary"]["rejected"] == 1

    assert len(report["top_candidates"]) == 2
