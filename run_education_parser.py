from parsers.education_parser import (
    extract_education,
    extract_certifications,
)


text = """
B.Tech in Computer Science from XYZ University (2021)

AWS Certified Developer - 2023

Certified Scrum Master

Completed training in Data Science and Machine Learning
"""

education = extract_education(text)

certifications = extract_certifications(text)

print("Education:", education)

print("Certifications:", certifications)