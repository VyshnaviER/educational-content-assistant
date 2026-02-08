#!/usr/bin/env python3
"""
FINAL EDUCATIONAL CONTENT ASSISTANT
Case-insensitive search and improved responses
"""
import os
import sys

print("=" * 60)
print("🎓 EDUCATIONAL CONTENT ASSISTANT - FINAL VERSION")
print("=" * 60)

class EducationalAssistant:
    def __init__(self):
        self.knowledge = []
        self.load_data()
    
    def load_data(self):
        """Load or create course materials"""
        data_dir = "data/sample_courses"
        
        if not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)
        
        # Ensure we have good sample content
        self.create_sample_content(data_dir)
        
        # Load all .txt files
        print(f"\n📚 Loading course materials from {data_dir}...")
        total_items = 0
        
        for filename in os.listdir(data_dir):
            if filename.endswith('.txt'):
                filepath = os.path.join(data_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Split into meaningful sections
                    sections = [s.strip() for s in content.split('\n\n') if s.strip()]
                    
                    for i, section in enumerate(sections):
                        self.knowledge.append({
                            'content': section,
                            'source': filename,
                            'section': i,
                            'content_lower': section.lower()  # Store lowercase for searching
                        })
                    
                    print(f"  • {filename}: {len(sections)} sections")
                    total_items += len(sections)
                    
                except Exception as e:
                    print(f"  • Error reading {filename}: {e}")
        
        print(f"📊 Total knowledge items: {total_items}")
        
        if total_items == 0:
            print("⚠️  No content loaded. Creating fresh samples...")
            self.create_sample_content(data_dir, force=True)
            self.load_data()  # Reload
    
    def create_sample_content(self, data_dir, force=False):
        """Create better sample content"""
        samples = {
            "biology_course.txt": """WHAT IS BIOLOGY?
Biology is the scientific study of life and living organisms.

BIOLOGY KEY CONCEPTS:
1. Cells: The basic unit of life
2. DNA: Carries genetic information  
3. Evolution: Species change over time
4. Homeostasis: Maintains internal balance

PHOTOSYNTHESIS:
Photosynthesis is the process by which plants convert sunlight into chemical energy.

CELLULAR BIOLOGY:
Cells are the fundamental units of all living things.""",
            
            "computer_science_course.txt": """COMPUTER SCIENCE INTRODUCTION
Computer Science is the study of computers and computational systems.

PROGRAMMING BASICS:
Programming involves writing instructions for computers to execute tasks.

KEY PROGRAMMING CONCEPTS:
- Variables: Store data values
- Functions: Reusable code blocks
- Algorithms: Step-by-step procedures
- Data Structures: Organize and store data

CAREERS IN COMPUTER SCIENCE:
1. Software Development
2. Data Science
3. Cybersecurity
4. Artificial Intelligence"""
        }
        
        for filename, content in samples.items():
            filepath = os.path.join(data_dir, filename)
            if not os.path.exists(filepath) or force:
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"  ✅ Created/updated: {filename}")
    
    def search(self, question, max_results=3):
        """Case-insensitive search for relevant content"""
        if not self.knowledge:
            return []
        
        question_lower = question.lower()
        results = []
        
        for item in self.knowledge:
            score = 0
            
            # Check each word in question
            for word in question_lower.split():
                if len(word) > 2:  # Skip very short words
                    # Check if word appears in content (case-insensitive)
                    if word in item['content_lower']:
                        # Higher score for exact matches
                        score += item['content_lower'].count(word) * 2
                    
                    # Check for partial matches
                    for content_word in item['content_lower'].split():
                        if word in content_word or content_word in word:
                            score += 0.5
            
            if score > 0:
                results.append({
                    'score': score,
                    'content': item['content'],
                    'source': item['source'],
                    'section': item['section']
                })
        
        # Sort by score (highest first)
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:max_results]
    
    def answer_question(self, question):
        """Generate answer for a question"""
        print(f"\n🤔 Question: {question}")
        
        # Search for relevant content
        results = self.search(question)
        
        if not results:
            # Try with simpler search
            simple_results = self.simple_search(question)
            if simple_results:
                results = simple_results
        
        if not results:
            return {
                'answer': "I couldn't find specific information about this topic in the course materials. Try asking about biology or computer science concepts.",
                'sources': [],
                'confidence': 'low'
            }
        
        # Generate answer
        answer = self.generate_answer(question, results)
        
        return {
            'answer': answer,
            'sources': [{'source': r['source'], 'section': r['section']} for r in results],
            'confidence': 'high' if len(results) > 0 else 'medium'
        }
    
    def simple_search(self, question):
        """Simpler keyword search for fallback"""
        question_lower = question.lower()
        keywords = ['biology', 'computer', 'programming', 'cell', 'photosynthesis', 'dna', 'evolution']
        
        for keyword in keywords:
            if keyword in question_lower:
                # Return items containing this keyword
                relevant = []
                for item in self.knowledge:
                    if keyword in item['content_lower']:
                        relevant.append({
                            'score': 10,
                            'content': item['content'],
                            'source': item['source'],
                            'section': item['section']
                        })
                return relevant[:2]  # Return top 2
        
        return []
    
    def generate_answer(self, question, results):
        """Generate answer from search results"""
        question_lower = question.lower()
        
        # Combine context from results
        context = "\n".join([r['content'] for r in results])
        
        # Try to extract a direct answer
        sentences = [s.strip() for s in context.replace('\n', '. ').split('.') if s.strip()]
        
        for sentence in sentences:
            sentence_lower = sentence.lower()
            
            # Look for definition-style sentences
            if any(word in sentence_lower for word in ['is the', 'are the', 'is a', 'are', 'means', 'defined as']):
                # Check if sentence relates to question
                question_words = [w for w in question_lower.split() if len(w) > 3]
                if any(qw in sentence_lower for qw in question_words):
                    return f"According to the course materials: {sentence}"
            
            # Look for sentences that start with key terms from question
            for word in question_lower.split():
                if len(word) > 4 and sentence_lower.startswith(word):
                    return f"Based on the course materials: {sentence}"
        
        # If no direct answer found, use topic-based responses
        if any(word in question_lower for word in ['biology', 'bio']):
            return "Biology is the scientific study of life and living organisms, including their structure, function, growth, and evolution."
        elif any(word in question_lower for word in ['computer', 'programming', 'code']):
            return "Computer Science involves the study of computers and computational systems, including programming, algorithms, and data structures."
        elif 'cell' in question_lower:
            return "Cells are the basic structural and functional units of all living organisms."
        elif 'photosynthesis' in question_lower:
            return "Photosynthesis is the process by which plants convert light energy into chemical energy to produce food."
        elif any(word in question_lower for word in ['dna', 'genetic']):
            return "DNA (Deoxyribonucleic acid) is the molecule that carries genetic instructions in living organisms."
        
        # Default: use first meaningful sentence from context
        for sentence in sentences:
            if len(sentence) > 20 and len(sentence) < 150:
                return f"Based on the course materials: {sentence}"
        
        # Fallback
        return f"I found relevant information about this topic in your course materials. Check the sources below for details."

def interactive_session():
    """Run interactive Q&A session"""
    assistant = EducationalAssistant()
    
    print("\n" + "=" * 40)
    print("💬 INTERACTIVE Q&A SESSION")
    print("=" * 40)
    print("\n💡 Try these questions (case doesn't matter):")
    print("  • what is biology?")
    print("  • explain computer science")
    print("  • tell me about cells")
    print("  • what is photosynthesis?")
    print("  • type 'quit' to exit")
    print("\n" + "=" * 40)
    
    while True:
        try:
            question = input("\n📝 Your question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you for using Educational Assistant!")
                break
            
            if not question:
                continue
            
            # Get answer
            result = assistant.answer_question(question)
            
            print(f"\n💡 Answer: {result['answer']}")
            
            if result['sources']:
                print(f"\n📚 Sources:")
                for source in result['sources']:
                    print(f"  • {source['source']} (Section: {source['section']})")
            
            print(f"\nConfidence: {result['confidence'].upper()}")
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

def quick_test():
    """Run a quick test"""
    print("\n🧪 Running quick test...")
    assistant = EducationalAssistant()
    
    test_questions = [
        "What is biology?",
        "Explain computer science",
        "Tell me about cells",
        "What is programming?",
        "What is photosynthesis?"
    ]
    
    for q in test_questions:
        result = assistant.answer_question(q)
        print(f"\nQ: {q}")
        print(f"A: {result['answer'][:80]}...")
        print(f"Sources: {len(result['sources'])} | Confidence: {result['confidence']}")
    
    print("\n✅ Test complete! Run without arguments for interactive mode.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        quick_test()
    else:
        interactive_session()
