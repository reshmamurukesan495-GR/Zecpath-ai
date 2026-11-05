from pypdf import PdfReader

from ats_engine.semantic_matcher import ( compute_similarity, classify_match )

#1. Read original PDF resume
pdf_path = "data/my_resume.pdf"

reader = PdfReader(pdf_path)

resume_text = ""

for page in reader.pages: 
    text = page.extract_text() 

    if text: resume_text += text + "\n"

#2. Software Engineer Job Description
job_description = """
We are looking for a Data Scientist.

Required skills:
Python, SQL, Machine Learning,
Deep Learning, Pandas, NumPy,
Scikit-learn and TensorFlow.

Responsibilities:
Build machine learning models,
analyse datasets, perform data cleaning,
develop predictive models and
communicate analytical insights.
"""

#3. Calculate semantic similarity
similarity = compute_similarity( resume_text, job_description )

final_score = similarity * 100

#4. Classify the match
match_type = classify_match(final_score)

#5. Display results
print("\n================================")
print("REAL PDF RESUME MATCHING RESULTS")
print("================================")

print("Resume:", pdf_path)

print("Similarity Score:", round(final_score, 2), "%")

print("Match Type:", match_type)

print("================================")

