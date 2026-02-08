"""
LLM manager for handling different language models
"""
import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LLMManager:
    """Manages LLM interactions for educational content"""
    
    def __init__(self, model_type: str = "mock"):
        """
        Initialize LLM manager
        
        Args:
            model_type: 'openai', 'huggingface', or 'mock' for testing
        """
        self.model_type = model_type
        
        if model_type == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                print("⚠️  OPENAI_API_KEY not found. Using mock responses.")
                self.model_type = "mock"
            else:
                import openai
                openai.api_key = api_key
                self.client = openai
                print("✅ OpenAI client initialized")
        
        elif model_type == "huggingface":
            print("🤗 HuggingFace models can be added for local inference")
            self.model_type = "mock"
        
        else:
            print("🤖 Using mock LLM for demonstration")
            self.model_type = "mock"
    
    def generate_response(self, prompt: str, 
                         model: str = "gpt-3.5-turbo",
                         temperature: float = 0.7,
                         max_tokens: int = 500) -> str:
        """
        Generate response using LLM or mock
        
        Args:
            prompt: Input prompt
            model: Model name
            temperature: Creativity (0-1)
            max_tokens: Max response length
        
        Returns:
            Generated response
        """
        if self.model_type == "mock":
            return self._mock_generation(prompt)
        
        elif self.model_type == "openai":
            try:
                response = self.client.ChatCompletion.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are an expert educational assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                print(f"❌ OpenAI error: {e}")
                return f"Error: {e}. Using mock response instead.\n\n{self._mock_generation(prompt)}"
        
        return self._mock_generation(prompt)
    
    def _mock_generation(self, prompt: str) -> str:
        """Generate mock response for testing"""
        # Simple mock responses based on prompt content
        if "biology" in prompt.lower():
            return """Based on the course materials, biology is the scientific study of living organisms and their interactions with the environment. 

Key concepts include:
1. Cells as the basic unit of life
2. DNA carrying genetic information
3. Evolution explaining biodiversity
4. Homeostasis maintaining internal balance

According to the textbook, understanding these fundamentals helps explain how living systems function at different levels of organization."""
        
        elif "photosynthesis" in prompt.lower():
            return """Photosynthesis is the process by which plants convert light energy into chemical energy (glucose). 

Process summary from course materials:
1. Light absorption by chlorophyll
2. Water splitting (photolysis)
3. Carbon dioxide fixation
4. Glucose production

Importance: This process produces oxygen and forms the base of most food chains."""
        
        elif "study guide" in prompt.lower():
            return """STUDY GUIDE: Biology Fundamentals

KEY CONCEPTS:
1. Cell Theory - All living things composed of cells
2. Energy Transfer - Photosynthesis & Respiration
3. Genetics - DNA, inheritance, variation
4. Evolution - Natural selection, adaptation

IMPORTANT TERMS:
- Homeostasis
- Metabolism
- Ecosystem
- Biodiversity

PRACTICE QUESTIONS:
1. Explain the difference between prokaryotic and eukaryotic cells
2. Describe the photosynthesis equation
3. What is natural selection?

Recommended study approach: Review concepts daily, create flashcards for terms, practice with diagrams."""
        
        else:
            return """Based on the provided course materials, here's a comprehensive answer:

The key concepts in the materials focus on fundamental biological principles. For optimal learning:

1. Review the main definitions and concepts
2. Connect related ideas across chapters
3. Practice applying concepts to examples
4. Use diagrams to visualize processes

Remember to cite specific examples from your course materials when studying for exams."""
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about current model setup"""
        return {
            "model_type": self.model_type,
            "requires_api_key": self.model_type == "openai",
            "status": "ready" if self.model_type != "openai" or os.getenv("OPENAI_API_KEY") else "needs_api_key"
        }

if __name__ == "__main__":
    # Test LLM Manager
    print("🧪 Testing LLM Manager...")
    
    # Test with mock
    llm = LLMManager("mock")
    test_prompt = "Explain biology in simple terms"
    response = llm.generate_response(test_prompt)
    
    print(f"\nTest Prompt: {test_prompt}")
    print(f"\nResponse:\n{response}")
    
    # Show model info
    print(f"\nModel Info: {llm.get_model_info()}")
