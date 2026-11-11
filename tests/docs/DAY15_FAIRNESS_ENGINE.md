DAY 15 – FAIRNESS ENGINE DOCUMENTATION
Title: Fairness & Bias Reduction

1. Objective
To ensure fair, unbiased, and standardized evaluation of candidates across diverse backgrounds.

The objective is to minimize the influence of personal attributes and improve the consistency of AI-based candidate scoring.

2. Key Strategies
2.1 Resume Normalization
Standardizes resume text format.
Removes formatting inconsistencies.
Converts text into lowercase.
Removes unnecessary special characters.
Normalizes spaces.
Standardizes resume headings.
Ensures uniform parsing.
2.2 Sensitive Data Masking
Masks non-essential personal information, including:

Name
Gender
Age
Location
Profile photos
Purpose:

Prevents unnecessary personal attributes from influencing AI-based candidate evaluation.

2.3 Keyword Bias Reduction
Reduces dependency on exact keyword matches.
Combines semantic understanding with skill matching.
Focuses on candidate skills and relevance.
Reduces over-dependence on keyword-based scoring.
Scoring Formula:

Fair Score = (0.6 × Semantic Score) + (0.4 × Skill Score)

Semantic similarity receives 60% weight, while skill matching receives 40% weight.

2.4 Score Normalization
Adjusts scores relative to the candidate pool.
Uses Min-Max normalization.
Converts scores into a common scale of 0–100.
Ensures consistent score comparison.
Formula:

Normalized Score = ((Candidate Score - Minimum Score) / (Maximum Score - Minimum Score)) × 100

If all candidates have identical scores, the normalized score is set to 100.

3. Bias Indicators Monitored
The following potential bias indicators are considered:

Overweighting specific keywords.
Education prestige bias.
Experience gap penalties.
Gender and location influence.
Dependence on personal attributes.
These indicators help identify areas that require additional fairness evaluation.

4. Fairness Principles
4.1 Equality
All candidates should be evaluated using consistent, job-related criteria.

4.2 Transparency
Scoring logic should be understandable and explainable.

4.3 Consistency
Standard scoring methods should be applied across candidate profiles.

4.4 Auditability
Candidate scoring logic should be traceable and reviewable.

5. Implementation Details
Main File:

ats_engine/fairness_engine.py

Functions Implemented:

normalize_scores()

Performs Min-Max score normalization.
mask_sensitive_data()

Masks sensitive candidate information.
reduce_keyword_bias()

Combines semantic and skill scores.
generate_fair_score()

Generates a bias-reduced candidate score.
Resume Normalization File:

parsers/normalization.py

Function:

normalize_resume_text()

This function standardizes resume text and improves consistency during parsing.

6. Testing and Validation
Testing Framework: Pytest

Test File:

tests/test_fairness_engine.py

The following test cases were implemented:

Score normalization.
Sensitive data masking.
Keyword bias reduction.
Fair candidate score generation.
Empty candidate handling.
Testing Command:

python -m pytest tests/test_fairness_engine.py -v
Test Results:

Total test cases: 5
Passed: 5
Failed: 0
Status: SUCCESS
All five test cases passed successfully.

7. Limitations
Rule-based fairness implementation at the initial stage.
Cannot completely eliminate hidden biases.
Depends on the quality of input data.
Requires additional fairness evaluation.
Score weighting may require adjustment based on recruitment requirements.
8. Future Improvements
Bias detection using machine learning.
Integration of advanced fairness metrics.
Implementation of adversarial debiasing models.
Fairness monitoring dashboards for recruiters.
Continuous evaluation of candidate scoring.
Improved explainability of AI-generated scores.
9. Conclusion
The Fairness Engine was developed as an important component of the Zecpath AI Applicant Tracking System.

It introduces resume normalization, sensitive data masking, keyword bias reduction, and candidate score normalization.

The implementation aims to improve consistency, transparency, and fairness in AI-based recruitment.

All five automated test cases passed successfully.