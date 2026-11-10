Day 13 – ATS Scoring Formula Design
1. Objective
To design a transparent and explainable ATS candidate scoring framework that evaluates candidates based on skills, experience, education and semantic similarity.

2. ATS Scoring Parameters
The scoring engine uses four parameters:

Parameter	Default Weight
Skills	35%
Experience	25%
Education	15%
Semantic Similarity	25%
Total	100%
3. Role-Based Weight Configuration
Different job roles use different scoring weights.

Backend Developer
Skills: 40%
Experience: 30%
Education: 10%
Semantic: 20%
Data Scientist
Skills: 35%
Experience: 25%
Education: 20%
Semantic: 20%
4. Candidate Score Generator
The candidate score generator calculates the final ATS score using the configured weights.

Example candidate:

Candidate ID: C123
Skills: 90
Experience: 85
Education: 80
Semantic Similarity: 88
Final ATS Score: 87.1%

5. Explainable Scoring Output
The system displays:

Candidate ID
Final ATS score
Weights used
Individual parameter scores
This makes the scoring process transparent.

6. Missing Data Handling
The system handles missing candidate information using safe score handling.

Missing values are converted to zero to prevent calculation errors.

Example:

Skills: 90
Experience: Missing
Education: 80
Semantic: 75
Final ATS Score: 59.0%

7. Testing
The following functionalities were tested:

Default weight configuration
Role-based scoring
ATS score calculation
Candidate score generation
Missing data handling
Previous project tests: 15 passed.

8. Deliverables
ATS scoring engine
Configurable weight system
Candidate score generator
Explainable scoring output
Missing data handling
Test implementation
9. Conclusion
The Day 13 ATS scoring framework was successfully implemented and tested.

The system provides configurable, transparent and explainable candidate scoring based on multiple recruitment parameters.

