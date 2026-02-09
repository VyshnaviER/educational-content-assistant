"""
LLM Manager for Google GenAI API
"""
import os
import google.genai as genai
from dotenv import load_dotenv

load_dotenv()

class LLMManager:
    def __init__(self, api_key=None):
        """Initialize Gemini API"""
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        self.client = genai.Client(api_key=self.api_key)
        print("✅ Gemini LLM initialized successfully")
    
    def generate_answer(self, question, context=None):
        """Generate answer using Gemini with optional context"""
        try:
            if context:
                prompt = f"""Based on the following educational context, answer the student's question:

CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""
            else:
                prompt = f"""Answer this educational question:

QUESTION: {question}

ANSWER:"""
            
            response = self.client.models.generate_content(
                model="models/gemini-2.0-flash",  # CORRECT MODEL NAME
                contents=prompt
            )
            
            return response.text.strip()
            
        except Exception as e:
            return f"Error generating answer: {str(e)}"
