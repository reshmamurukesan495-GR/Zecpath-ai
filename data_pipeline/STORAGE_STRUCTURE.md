# Storage Structure

## 1. Resumes

Store original candidate resumes uploaded by candidates.

Example:

data/resumes/
- candidate_001.pdf
- candidate_002.docx

## 2. Parsed Profiles

Store structured candidate information extracted from resumes.

Example:

{
    "candidate_id": "C001",
    "name": "John Smith",
    "skills": ["Python", "SQL"],
    "experience": "2 years",
    "education": "MSc Data Science"
}

## 3. ATS Scores

Store ATS matching results between candidates and job descriptions.

Example:

{
    "candidate_id": "C001",
    "job_id": "J001",
    "ats_score": 85
}

## 4. Screening Reports

Store candidate screening results and eligibility information.

## 5. Interview Results

Store interview scores, feedback, and evaluation results.

Example:

{
    "candidate_id": "C001",
    "job_id": "J001",
    "interview_score": 88,
    "feedback": "Good technical knowledge"
}
