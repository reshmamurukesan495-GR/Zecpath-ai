Day 12 – Semantic Matching Engine
Zecpath AI
1. Objective
To move beyond keyword matching and enable deep semantic resume-to-job matching using transformer-based embeddings.

2. Technologies Used
Python
Sentence Transformers
Scikit-learn
NumPy
Pytest
3. Semantic Matching Approach
The system uses the pretrained all-MiniLM-L6-v2 model to convert resume and job description text into numerical embeddings.

Cosine similarity is used to measure the semantic similarity between the texts.

4. Key Features
Embedding-Based Matching

Converts text into embeddings.
Captures semantic meaning rather than relying only on keywords.
Multi-Dimensional Matching The system compares:

Skills
Experience summaries
Project descriptions
Weighted Final Score

Skills similarity: 40%
Experience similarity: 30%
Project similarity: 30%
5. Match Classification
Score >= 85: Strong Match
Score >= 65: Moderate Match
Score < 65: Weak Match
6. Sample Execution Result
The sample resume and job description produced the following results:

Skills similarity: 87.21%
Experience similarity: 100%
Project similarity: 47.75%
Final similarity score: 79.21%
Match type: Moderate Match
7. Matching Accuracy Report
Sample test dataset:

Total resumes tested: 15
Domains: Software Development, Data Science and Marketing
Reported results:

Average similarity score: 87%
Strong matches correct: 90%
Moderate matches correct: 85%
Weak matches correct: 80%
Overall accuracy: 88%
These are the results reported by the sample evaluation script and should not be interpreted as independently verified real-world accuracy.

8. Improvements Suggested
Use domain-specific embedding models.
Fine-tune similarity weights dynamically.
Incorporate recruiter feedback.
9. Conclusion
The Semantic Matching Engine improves resume screening by comparing the meaning of resume content with job descriptions. It provides section-wise similarity scores, a weighted final score and match classification.

