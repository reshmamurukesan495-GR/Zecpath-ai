Day 14 – Candidate Ranking & Shortlisting
1. Objective  

To automate candidate ranking, filtering and shortlisting based on ATS scores.

2. Key Features

2.1 Auto-Ranking Engine

Sorts candidates by final ATS score.
Assigns ranks automatically.
Displays candidates in descending order.
2.2 Shortlisting Automation

Candidates are classified based on their final scores.

Score Range	Status
75 and above	Shortlisted
50–74	Review
Below 50	Rejected

2.3 Top Candidate Selection
Selects the top five shortlisted candidates by default.
Supports recruiter candidate selection.

2.4 Recruiter-Friendly Output
Generates a report containing:

Job ID
Total candidates
Shortlisted candidates
Candidates under review
Rejected candidates
Top candidate details and scores

3. Implementation

Main file: ats_engine/ranking_engine.py

Supporting files:

tests/test_ranking_engine.py
run_ranking.py

4. Testing

Automated tests were implemented using Pytest.

Test cases:

Candidate ranking test.
Shortlisting classification test.
Recruiter report generation test.
All three tests passed successfully.

5. Execution

Command:

python run_ranking.py

The execution script successfully generated the recruiter-friendly report.


6. Advantages

Automates candidate ranking.
Saves recruiter time.
Provides consistent shortlisting decisions.
Improves recruitment workflow.
Generates clear candidate reports.

7. Conclusion

The Day 14 Candidate Ranking and Shortlisting module was successfully implemented and tested.

The system provides automated candidate ranking, score-based classification, top candidate selection and recruiter-friendly reporting.

