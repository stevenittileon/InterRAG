# InterRAG: Resume-based Interview Q&A Generator

InterRAG is a Retrieval-Augmented Generation (RAG) tool that helps you prepare for interviews by:
- Generating tailored interview questions based on your resume (PDF)
- Generating optimal, human-like answers for each question using your resume as context

## Features

- **PDF Resume Input:** Just provide your resume as a PDF file.
- **Automatic Question Generation:** Get interview questions tailored to your experience and domain.
- **Contextual Answer Generation:** Receive realistic, concise answers (10–15 sentences) for each question, grounded in your resume.
- **Cerebras LLM Integration:** Uses the Cerebras Model Studio API for high-quality language generation.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Set Up Python Environment

```bash
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install cerebras.cloud.sdk
```

### 3. Run the Script

```bash
python test_rag_answer.py
```

- When prompted, enter the path to your resume PDF file (e.g., `/Users/yourname/Desktop/resume.pdf`).
- If you haven't set your Cerebras API key as an environment variable, you'll be prompted to enter it.

---

## Requirements

- Python 3.10 or 3.11
- [Cerebras Model Studio API Key](https://modelz.cerebras.net/)
- See `requirements.txt` for Python dependencies

---

## How It Works

1. **Extracts text from your PDF resume**
2. **Generates interview questions tailored to your experience**
3. **Generates optimal, human-like answers for each question using your resume as context**

---

## Example Usage

```bash
python test_rag_answer.py
```
```
Enter the path to your resume PDF file: /Users/yourname/Desktop/resume.pdf
Enter your CEREBRAS_API_KEY: sk-...
```

_Output:_
```
Question:
Can you tell me about a time when you had to provide excellent customer service in a fast-paced environment? How did you handle it?

Answer:
[Generated answer based on your resume]

----------------------------------------
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Cerebras Model Studio](https://modelz.cerebras.net/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
