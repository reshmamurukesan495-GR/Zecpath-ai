import re
from pathlib import Path

from pypdf import PdfReader
from docx import Document

from utils.logger import logger


def extract_from_pdf(file_path):
    """Extract text from a PDF resume."""
    logger.info("PDF extraction started")

    reader = PdfReader(file_path)
    text = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)

    result = "\n".join(text)

    logger.info("PDF extraction completed")
    return result


def extract_from_docx(file_path):
    """Extract text from a DOCX resume."""
    logger.info("DOCX extraction started")

    document = Document(file_path)
    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    result = "\n".join(text)

    logger.info("DOCX extraction completed")
    return result


def clean_text(text):
    """Clean extracted resume text."""
    text = text.replace("\r", "\n")

    # Remove excessive spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text.strip()


def extract_resume(file_path):
    """Extract and clean text from a PDF or DOCX resume."""
    file_path = Path(file_path)

    if file_path.suffix.lower() == ".pdf":
        text = extract_from_pdf(file_path)

    elif file_path.suffix.lower() == ".docx":
        text = extract_from_docx(file_path)

    else:
        raise ValueError("Only PDF and DOCX files are supported.")

    text = clean_text(text)
    text = normalize_text(text)

    return text

def normalize_text(text):
    """Normalize resume text."""
    # Normalize bullet points
    text=text.replace(".","-")
    text = text.replace("▪", "-")
    text = text.replace("●", "-")

# Normalize section headings
    sections =[
        "RESUME",
        'PROFILE',
        'SUMMARY',
        'EDUCATION',
        'EXPERIENCE',
        'SKILLS',
        'CERTICATION',
        'PROJECTS'
    ]

    for section in sections:
        text=re.sub(
           rf"(?i)\b{section}\b",
           section,
           text
        )
    
    return text.strip()