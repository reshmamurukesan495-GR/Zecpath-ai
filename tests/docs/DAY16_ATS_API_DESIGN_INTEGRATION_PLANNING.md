1. ATS API Specification
Base URL
https://api.zecpath.ai/v1/

1. Resume Upload API

Endpoint
POST /resume/upload

Request (multipart/form-data)
{
"file": "resume.pdf",
"job_id": "J123",
"candidate_id": "C123"
}

Response
{
"status": "success",
"message": "Resume uploaded successfully",
"resume_id": "R456",
"timestamp": "2026-04-18T10:00:00Z"
}

2. Resume Parsing API

Endpoint
POST /resume/parse

Request
{
"resume_id": "R456"
}

Response
{
"candidate_id": "C123",
"parsed_profile": {
"skills": ["Python", "Django"],
"experience": [...],
"education": [...]

},
"status": "completed"
}

3. ATS Scoring API

Endpoint
POST /ats/score

Request
{
"candidate_id": "C123",
"job_id": "J123"
}

Response
{
"candidate_id": "C123",
"final_score": 86.5,
"breakdown": {
"skills": 90,
"experience": 85,
"education": 80,
"semantic": 88
}
}

4. Shortlisting API

Endpoint
POST /ats/shortlist

Request
{
"job_id": "J123"
}

Response
{
"job_id": "J123",
"total_candidates": 50,
"shortlisted": 20,
"candidates": [
{
"candidate_id": "C123",

"score": 88,
"status": "Shortlisted"
}
]
}

2. Async Job Handling Design

Async Flow

Resume Upload
↓
Job Queue (Redis / Kafka)
↓
Worker Service (Parser + ATS Engine)
↓
Store Results in DB
↓
Webhook / Polling API Response

Async API Example

Start Processing
POST /jobs/start

Response
{
"job_id": "JOB789",
"status": "processing"
}

Check Status
GET /jobs/status/JOB789

Response
{
"job_id": "JOB789",
"status": "completed",
"result_url": "/ats/result/C123"
}

3. Input / Output Schemas

Candidate Schema

{
"candidate_id": "C123",
"resume_id": "R456",
"skills": ["Python", "Django"],
"experience": [],
"education": []
}


Job Schema

{
"job_id": "J123",
"job_title": "Backend Developer",
"required_skills": ["Python", "Django"],
"experience_required": 3
}

Score Schema

{
"candidate_id": "C123",
"job_id": "J123",
"final_score": 86.5,
"status": "Shortlisted"
}

4. Error Handling Standards

Error Response Format
{
"status": "error",
"error_code": "INVALID_INPUT",
"message": "Missing candidate_id",
"timestamp": "2026-04-18T10:05:00Z"
}

Common Error Codes

Code                  Description
INVALID_INPUT         Missing/invalid data
NOT_FOUND             Resource not found
PROCESSING_ERR AI     processing failure
SERVER_ERROR          Internal system error

5. Logging Standards

Log Format

{
"timestamp": "2026-04-18T10:10:00Z",
"service": "ATS Engine",
"level": "INFO",
"message": "Candidate scoring completed",
"candidate_id": "C123",
"job_id": "J123"
}

Logging Levels

• INFO → Normal operations
• WARNING → Minor issues
• ERROR → Failures
• DEBUG → Development logs

6. Integration Flow Document

Title: ATS API Integration Flow – Zecpath

Step-by-Step Flow

Frontend → Upload Resume
↓
Backend → Call /resume/upload
↓
Backend → Call /resume/parse
↓
Backend → Call /ats/score
↓
Backend → Call /ats/shortlist
↓
Frontend → Display Results


Backend ↔ AI Communication

• REST APIs for synchronous calls
• Queue-based processing for heavy tasks
• Webhooks for async updates

Data Flow Summary

1. Resume uploaded
2. Parsed into structured profile
3. Scored using ATS engine
4. Ranked and shortlisted
5. Returned to recruiter dashboard

7. Optional FastAPI Starter (Bonus)

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
return {"message": "Zecpath ATS API Running"}