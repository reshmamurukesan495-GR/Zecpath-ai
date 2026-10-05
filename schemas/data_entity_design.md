# Zecpath AI – Data Entity Design

## 1. Candidate Profile

- Candidate ID
- Name
- Email
- Phone
- Location
- Skills
- Education
- Experience
- Certifications

## 2. Job Profile

- Job ID
- Job Title
- Department
- Location
- Employment Type
- Required Skills
- Preferred Skills
- Experience Required
- Education Required
- Certifications

## 3. Skill Object

- Skill Name
- Skill Category
- Skill Level
- Years of Experience

## 4. Experience Object

- Company
- Job Title
- Start Date
- End Date
- Responsibilities
- Technologies Used

### Example

```json
{
  "company": "ABC Technologies",
  "job_title": "Data Scientist",
  "start_date": "2023-01",
  "end_date": "2025-01",
  "responsibilities": [
    "Developed machine learning models",
    "Performed data analysis",
    "Created Power BI dashboards"
  ],
  "technologies_used": [
    "Python",
    "SQL",
    "Power BI",
    "Machine Learning"
  ]
}




## 1. Candidate Profile

The Candidate Profile represents a job applicant.

### Fields

- Candidate ID
- Name
- Email
- Phone
- Location
- Skills
- Education
- Experience
- Certifications
- Professional Summary

---

## 2. Job Profile

The Job Profile represents a job vacancy.

### Fields

- Job ID
- Job Title
- Department
- Location
- Employment Type
- Required Skills
- Preferred Skills
- Experience Required
- Education Required
- Certifications
- Job Description

---

## 3. Skill Object

The Skill Object represents an individual skill possessed by a candidate or required for a job.

### Fields

- Skill Name
- Skill Category
- Skill Level
- Years of Experience

### Example

```json
{
  "skill_name": "Python",
  "skill_category": "Technical",
  "skill_level": "Intermediate",
  "years_of_experience": 2
}


### Example

```json
{
  "company": "ABC Technologies",
  "job_title": "Data Scientist",
  "start_date": "2023-01",
  "end_date": "2025-01",
  "responsibilities": [
    "Developed machine learning models",
    "Analyzed business data"
  ],
  "technologies_used": [
    "Python",
    "SQL",
    "Power BI"
  ]
}


