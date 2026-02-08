"""
Simple generator for educational content
"""

def generate_answer(question, context=None):
    """Generate simple answers based on question keywords"""
    
    # Dictionary of predefined answers
    responses = {
        "biology": "Biology is the scientific study of life and living organisms.",
        "programming": "Programming is writing instructions for computers to execute tasks.",
        "photosynthesis": "Photosynthesis is the process plants use to convert sunlight into chemical energy.",
        "cell": "Cells are the basic structural and functional units of all living organisms.",
        "variable": "Variables are containers for storing data values in programming.",
        "function": "Functions are reusable blocks of code that perform specific tasks.",
        "algorithm": "Algorithms are step-by-step procedures for solving problems.",
        "evolution": "Evolution is the process by which species change over time through natural selection."
    }
    
    question_lower = question.lower()
    
    # Check for keywords in the question
    for keyword, answer in responses.items():
        if keyword in question_lower:
            if context:
                return f"Based on the course materials: {answer}"
            return answer
    
    # Default response
    if context:
        return f"Based on the course materials: {question} is an important concept. Review the provided materials for detailed information."
    
    return f"{question} is an important topic in education. Please consult your course materials for specific information."

if __name__ == "__main__":
    # Test the generator
    test_questions = [
        "What is biology?",
        "Explain programming",
        "What are cells?"
    ]
    
    print("🧪 Testing Simple Generator")
    print("=" * 40)
    
    for question in test_questions:
        answer = generate_answer(question)
        print(f"Q: {question}")
        print(f"A: {answer}")
        print()
