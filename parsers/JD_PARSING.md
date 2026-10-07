# Job Description Parsing System

## Objective

The Job Description Parsing System converts unstructured job descriptions into structured AI-readable job requirement objects.

## Input

The system accepts a job description text file.

Example:

- Job title
- Required skills
- Experience requirements
- Education requirements
- Responsibilities

## Processing Steps

### 1. Read Job Description

The parser reads the job description from the input file.

### 2. Extract Role

The system identifies the job role or position.

Example:

Data Scientist

### 3. Extract Required Skills

The system extracts technical skills from the job description.

Example:

- Python
- SQL
- Machine Learning
- Power BI
- Pandas
- NumPy

### 4. Extract Experience

The system identifies the required experience.

Example:

2 years of experience in data science or machine learning.

### 5. Extract Education

The system identifies the required educational qualification.

Example:

MSc in Data Science, MSc Computer Science, or BTech.

### 6. Create Structured Output

The extracted information is stored as a structured JSON object.

## Output Structure

```json
{
    "role": "Data Scientist",
    "required_skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "Power BI",
        "Pandas",
        "NumPy"
    ],
    "experience_required": "2 years of experience in data science or machine learning.",
    "education_required": "MSc in Data Science, MSc Computer Science, or BTech."
}
