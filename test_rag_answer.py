from rag.generator import QuestionGenerator
from rag.pdf_parser import extract_text_from_pdf
import re
import sys

pdf_path = input("Enter the path to your resume PDF file: ").strip()
try:
    resume_text = extract_text_from_pdf(pdf_path)
except Exception as e:
    print(f"Could not read resume PDF file: {e}")
    sys.exit(1)

if not resume_text.strip():
    print("Resume not found or PDF is empty. Please provide a valid resume PDF.")
    sys.exit(1)

domain = "general"
generator = QuestionGenerator()

# Step 1: Generate interview questions
questions_text = generator.generate(resume_text, domain)

# Step 2: Extract questions
questions = re.findall(r"\d+\.\s*(.*?)(?=\n\d+\.|$)", questions_text, re.DOTALL)

# Step 3: Generate and print answers for each question
for question in questions:
    answer = generator.generate_answer(resume_text, question, domain)
    print("Question:")
    print(question.strip())
    print("\nAnswer:")
    print(answer.strip())
    print("\n" + "-"*40 + "\n") 