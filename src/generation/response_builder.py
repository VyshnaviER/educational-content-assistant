"""
Builds formatted responses with citations
"""
from typing import List, Dict, Any
from .prompt_templates import EducationalPrompts

class ResponseBuilder:
    """Builds educational responses with proper formatting"""
    
    def __init__(self):
        self.prompts = EducationalPrompts()
    
    def build_qa_response(self, question: str, 
                         context_chunks: List[Dict[str, Any]],
                         student_level: str = "intermediate") -> Dict[str, Any]:
        """
        Build a Q&A response with citations
        
        Args:
            question: Student's question
            context_chunks: Retrieved context chunks
            student_level: beginner/intermediate/advanced
        
        Returns:
            Formatted response dictionary
        """
        # Combine context from chunks
        context = self._combine_context(context_chunks)
        
        # Get sources for citation
        sources = self._extract_sources(context_chunks)
        
        # Choose prompt based on level
        if student_level == "beginner":
            prompt_type = "beginner"
        elif student_level == "advanced":
            prompt_type = "advanced"
        else:
            prompt_type = "detailed"
        
        # Build prompt
        prompt = self.prompts.get_prompt(
            prompt_type,
            context=context,
            question=question
        )
        
        return {
            "question": question,
            "context_used": context[:500] + "..." if len(context) > 500 else context,
            "sources": sources,
            "student_level": student_level,
            "prompt": prompt[:200] + "..." if len(prompt) > 200 else prompt,
            "metadata": {
                "chunks_used": len(context_chunks),
                "total_context_length": len(context)
            }
        }
    
    def build_study_guide(self, topic: str,
                         context_chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Build a study guide
        
        Args:
            topic: Study topic
            context_chunks: Retrieved context chunks
        
        Returns:
            Study guide dictionary
        """
        context = self._combine_context(context_chunks)
        sources = self._extract_sources(context_chunks)
        
        prompt = self.prompts.get_prompt(
            "study_guide",
            context=context,
            topic=topic
        )
        
        return {
            "topic": topic,
            "context_used": context[:500] + "..." if len(context) > 500 else context,
            "sources": sources,
            "prompt": prompt[:200] + "..." if len(prompt) > 200 else prompt,
            "metadata": {
                "chunks_used": len(context_chunks),
                "total_context_length": len(context)
            }
        }
    
    def _combine_context(self, chunks: List[Dict[str, Any]]) -> str:
        """Combine multiple context chunks"""
        context_parts = []
        for i, chunk in enumerate(chunks):
            content = chunk.get('content', '')
            metadata = chunk.get('metadata', {})
            
            # Add source reference
            source_ref = f"[Source: {metadata.get('source', 'unknown')}"
            if 'page' in metadata:
                source_ref += f", Page: {metadata['page']}"
            source_ref += "]"
            
            context_parts.append(f"{source_ref}\n{content}\n")
        
        return "\n---\n".join(context_parts)
    
    def _extract_sources(self, chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract source information from chunks"""
        sources = []
        for chunk in chunks:
            metadata = chunk.get('metadata', {})
            source_info = {
                "source": metadata.get('source', 'Unknown'),
                "page": metadata.get('page', 'N/A'),
                "type": metadata.get('type', 'Unknown'),
                "content_preview": chunk.get('content', '')[:100] + "..."
            }
            if source_info not in sources:
                sources.append(source_info)
        return sources
    
    def format_final_response(self, llm_response: str, 
                            response_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format final response with all metadata
        
        Args:
            llm_response: Generated response from LLM
            response_data: Response builder data
        
        Returns:
            Complete formatted response
        """
        return {
            "answer": llm_response,
            "question": response_data.get("question", ""),
            "sources": response_data.get("sources", []),
            "metadata": {
                **response_data.get("metadata", {}),
                "student_level": response_data.get("student_level", "intermediate"),
                "timestamp": self._get_timestamp()
            },
            "confidence": self._estimate_confidence(llm_response)
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def _estimate_confidence(self, response: str) -> float:
        """Estimate confidence score for response"""
        # Simple confidence estimation
        if "I don't have enough information" in response:
            return 0.1
        elif "Error" in response:
            return 0.0
        elif len(response) > 100 and "." in response:
            return 0.8
        else:
            return 0.5

if __name__ == "__main__":
    # Test Response Builder
    print("🧪 Testing Response Builder...")
    
    builder = ResponseBuilder()
    
    # Create mock context chunks
    mock_chunks = [
        {
            "content": "Biology is the study of living organisms. Cells are the basic unit of life.",
            "metadata": {"source": "biology_textbook.pdf", "page": 1, "type": "pdf"}
        },
        {
            "content": "Photosynthesis converts light energy to chemical energy in plants.",
            "metadata": {"source": "biology_textbook.pdf", "page": 45, "type": "pdf"}
        }
    ]
    
    # Test Q&A response
    qa_data = builder.build_qa_response(
        "What is biology?",
        mock_chunks,
        "beginner"
    )
    
    print("\n✅ Q&A Response Data:")
    for key, value in qa_data.items():
        if key != "prompt":
            print(f"{key}: {value}")
    
    # Test study guide
    study_data = builder.build_study_guide("Biology Basics", mock_chunks)
    
    print("\n✅ Study Guide Data:")
    for key, value in study_data.items():
        if key != "prompt":
            print(f"{key}: {value}")
