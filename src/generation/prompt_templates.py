"""
Prompt templates for educational Q&A
"""
from typing import Dict, List

class EducationalPrompts:
    """Prompt templates for different educational levels and contexts"""
    
    BASIC_QA_TEMPLATE = """You are an expert educational assistant. Use the provided context to answer the student's question clearly and accurately.

Context from course materials:
{context}

Student's Question: {question}

Instructions:
1. Answer based ONLY on the provided context
2. If the answer isn't in the context, say "I don't have enough information in the course materials to answer this question accurately."
3. Keep explanations clear and concise
4. Mention key terms from the context
5. If relevant, cite the source (e.g., "According to the course materials...")

Answer:"""

    DETAILED_EXPLANATION_TEMPLATE = """You are a patient tutor explaining concepts to a student. Use the provided educational context to give a detailed, step-by-step explanation.

Educational Context:
{context}

Student's Question: {question}

Provide a comprehensive explanation:
1. Start with a simple definition
2. Break down the concept into key components
3. Give examples if available in context
4. Explain the importance/relevance
5. Summarize the main points

Remember: Stay within the provided context. If information is missing, acknowledge it.

Detailed Explanation:"""

    STUDY_GUIDE_TEMPLATE = """Create a study guide based on the following course materials.

Course Materials Context:
{context}

Topic/Subject: {topic}

Create a study guide with:
1. Key concepts and definitions
2. Important formulas/theorems (if any)
3. Main points to remember
4. Common questions/application areas
5. Recommended practice approach

Study Guide:"""

    def get_prompt(self, prompt_type: str = "basic", **kwargs) -> str:
        """Get formatted prompt based on type"""
        templates = {
            "basic": self.BASIC_QA_TEMPLATE,
            "detailed": self.DETAILED_EXPLANATION_TEMPLATE,
            "study_guide": self.STUDY_GUIDE_TEMPLATE
        }
        
        if prompt_type not in templates:
            prompt_type = "basic"
        
        template = templates[prompt_type]
        
        try:
            return template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required parameter: {e}")

if __name__ == "__main__":
    prompts = EducationalPrompts()
    print("✅ Prompt templates created successfully!")
