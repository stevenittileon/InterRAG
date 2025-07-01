# UnSloth LLM generator
import os
import requests
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv

load_dotenv()

class QuestionGenerator:
    def __init__(self, model_name='llama-4-scout-17b-16e-instruct'):
        self.api_key = os.getenv('CEREBRAS_API_KEY')
        if not self.api_key:
            self.api_key = input("Enter your CEREBRAS_API_KEY: ").strip()
            if not self.api_key:
                raise ValueError("CEREBRAS_API_KEY is required to use the Cerebras API.")
        self.model_name = model_name
        self.client = Cerebras(api_key=self.api_key)

    def generate(self, resume_text, domain=None):
        system_prompt = (
            "You are an expert interview coach. Given the following resume (domain: {}), "
            "generate 5 tailored interview questions that would help the candidate prepare for interviews in this field."
        ).format(domain)
        user_prompt = f"Resume:\n{resume_text}\nQuestions:"
        stream = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model=self.model_name,
            stream=True,
            max_completion_tokens=512,
            temperature=0.2,
            top_p=0.95
        )
        output = ""
        for chunk in stream:
            output += chunk.choices[0].delta.content or ""
        return output

    def generate_answer(self, resume_text, question, domain=None):
        system_prompt = (
            "You are an expert interview coach. Given the following resume (domain: {}), "
            "answer the interview question in a concise, human-like way, using the resume as supporting context. "
            "Your answer should be realistic, based on the resume, and no longer than 10-15 sentences to mimic a real-world interview response."
        ).format(domain)
        user_prompt = (
            f"Resume:\n{resume_text}\n"
            f"Interview Question: {question}\n"
            f"Answer:"
        )
        stream = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model=self.model_name,
            stream=True,
            max_completion_tokens=512,
            temperature=0.7,
            top_p=0.95
        )
        output = ""
        for chunk in stream:
            output += chunk.choices[0].delta.content or ""
        return output 