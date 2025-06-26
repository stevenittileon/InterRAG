import sys
from rag.pdf_parser import extract_text_from_pdf
from rag.domain_detector import detect_domain
from rag.generator import QuestionGenerator

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <resume.pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    print(f"Extracting text from {pdf_path}...")
    resume_text = extract_text_from_pdf(pdf_path)
    print("Detecting domain...")
    domain = detect_domain(resume_text)
    print(f"Detected domain: {domain}")

    print("Generating interview questions based on your resume...")
    generator = QuestionGenerator()
    questions = generator.generate(resume_text, domain)
    print("\nGenerated Interview Questions:\n")
    print(questions) 