"""
Main generation module - orchestrates the RAG pipeline
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from generation.llm_manager import LLMManager
from generation.response_builder import ResponseBuilder
from generation.prompt_templates import EducationalPrompts

class EducationalGenerator:
    """Main educational content generator"""
    
    def __init__(self, model_type: str = "mock"):
        self.llm = LLMManager(model_type)
        self.builder = ResponseBuilder()
        self.prompts = EducationalPrompts()
    
    def answer_question(self, question: str, 
                       context_chunks: list,
                       student_level: str = "intermediate") -> dict:
        """
        Answer a student's question using RAG
        
        Args:
            question: Student's question
            context_chunks: Retrieved context from vector store
            student_level: beginner/intermediate/advanced
        
        Returns:
            Complete answer with metadata
        """
        print(f"\n🎓 Processing question: '{question}'")
        print(f"   Student level: {student_level}")
        print(f"   Context chunks: {len(context_chunks)}")
        
        # Build response data
        response_data = self.builder.build_qa_response(
            question, context_chunks, student_level
        )
        
        # Generate answer using LLM
        llm_response = self.llm.generate_response(response_data['prompt'])
        
        # Format final response
        final_response = self.builder.format_final_response(llm_response, response_data)
        
        print(f"✅ Answer generated (confidence: {final_response['confidence']:.1%})")
        return final_response
    
    def create_study_guide(self, topic: str, context_chunks: list) -> dict:
        """
        Create a study guide
        
        Args:
            topic: Study topic
            context_chunks: Retrieved context
        
        Returns:
            Study guide with metadata
        """
        print(f"\n📚 Creating study guide for: '{topic}'")
        print(f"   Context chunks: {len(context_chunks)}")
        
        # Build study guide data
        study_data = self.builder.build_study_guide(topic, context_chunks)
        
        # Generate study guide using LLM
        llm_response = self.llm.generate_response(study_data['prompt'])
        
        # Format response
        return {
            "study_guide": llm_response,
            "topic": topic,
            "sources": study_data['sources'],
            "metadata": study_data['metadata']
        }
    
    def get_system_info(self) -> dict:
        """Get information about the generation system"""
        return {
            "llm_info": self.llm.get_model_info(),
            "templates_available": ["basic", "detailed", "study_guide", 
                                   "cross_disciplinary", "beginner", 
                                   "advanced", "exam_prep"],
            "status": "ready"
        }

def test_generation_system():
    """Test the complete generation system"""
    print("=" * 60)
    print("🧪 TESTING EDUCATIONAL GENERATION SYSTEM")
    print("=" * 60)
    
    # Initialize generator
    generator = EducationalGenerator("mock")
    
    # Get system info
    info = generator.get_system_info()
    print(f"\n📊 System Info:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    # Create mock context
    mock_context = [
        {
            "content": "Computer Science is the study of computers and computational systems. Programming involves writing instructions for computers to execute.",
            "metadata": {"source": "cs_basics.txt", "page": 1, "type": "textbook"}
        },
        {
            "content": "Python is a popular programming language known for its simplicity. Variables store data, functions are reusable code blocks.",
            "metadata": {"source": "cs_basics.txt", "page": 5, "type": "textbook"}
        }
    ]
    
    # Test question answering
    print("\n" + "=" * 40)
    print("1. TESTING Q&A SYSTEM")
    print("=" * 40)
    
    question = "What is computer science?"
    answer = generator.answer_question(question, mock_context, "beginner")
    
    print(f"\n❓ Question: {answer['question']}")
    print(f"\n💡 Answer:\n{answer['answer']}")
    print(f"\n📚 Sources:")
    for source in answer['sources']:
        print(f"  • {source['source']} (Page: {source['page']})")
    
    # Test study guide generation
    print("\n" + "=" * 40)
    print("2. TESTING STUDY GUIDE GENERATOR")
    print("=" * 40)
    
    study_guide = generator.create_study_guide("Programming Basics", mock_context)
    
    print(f"\n📖 Topic: {study_guide['topic']}")
    print(f"\n📋 Study Guide:\n{study_guide['study_guide']}")
    
    print("\n" + "=" * 60)
    print("✅ GENERATION SYSTEM TEST COMPLETE")
    print("=" * 60)
    
    return generator

if __name__ == "__main__":
    test_generation_system()
