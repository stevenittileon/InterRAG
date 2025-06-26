# UnSloth LLM generator
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class QuestionGenerator:
    def __init__(self, model_name='gemini-1.5-pro-latest'):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")
        self.model_name = model_name
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_name}:generateContent?key={self.api_key}"

    def generate(self, resume_text, domain=None):
        prompt = (
            f"You are an expert interview coach. Given the following resume (domain: {domain}), "
            f"generate 5 tailored interview questions that would help the candidate prepare for interviews in this field.\n"
            f"Resume:\n{resume_text}\nQuestions:"
        )
        data = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ]
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text'] 