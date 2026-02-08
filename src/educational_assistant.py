#!/usr/bin/env python3
"""
EDUCATIONAL CONTENT ASSISTANT - FINAL WORKING VERSION
Simple but fully functional RAG system
"""
import os
import sys
import json

print("=" * 60)
print("🎓 EDUCATIONAL CONTENT ASSISTANT")
print("=" * 60)

class KnowledgeBase:
    """Simple knowledge base for educational content"""
    
    def __init__(self):
        self.data = []
        self.loaded = False
    
    def load_courses(self, data_dir="data/sample_courses"):
        """Load course materials from directory"""
        print(f"\n📚 Loading course materials from {data_dir}...")
        
        if not os.path.exists(data_dir):
            print(f"❌ Directory not found. Creating {data_dir}...")
            os.makedirs(data_dir, exist_ok=True)
            self._create_sample_content(data_dir)
        
        files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
        
        if not files:
            print("⚠️  No course files found. Creating samples...")
            self._create_sample_content(data_dir)
            files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
        
        print(f"📄 Found {len(files)} course files:")
        
        self.data = []
        for filename in files:
            filepath = os.path.join(data_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Split into sections
                sections = [s.strip() for s in content.split('\n\n') if s.strip()]
                
                for i, section in enumerate(sections):
                    self.data.append({
                        'content': section,
                        'source': filename,
                        'section_id': i
                    })
                
                print(f"  • {filename}: {len(sections)} sections")
                
            except Exception as e:
                print(f"  • Error reading {filename}: {e}")
        
        print(f"📊 Total knowledge items: {len(self.data)}")
        self.loaded = True
        return True
    
    def _create_sample_content(self, data_dir):
        """Create sample course content"""
        samples = {
            "biology_basics.txt": """INTRODUCTION TO BIOLOGY

Biology is the scientific study of life and living organisms.

KEY CONCEPTS:
1. Cells: Basic units of life
2. DNA: Carries genetic information
3. Evolution: Species change over time
4. Ecosystems: Communities of organisms

IMPORTANT PROCESSES:
- Photosynthesis: Plants make food from sunlight
- Cellular Respiration: Cells produce energy
- Mitosis: Cell division for growth

STUDY TIP: Relate concepts to real-world examples.""",
            
            "computer_science.txt": """COMPUTER SCIENCE FUNDAMENTALS

Programming is writing instructions for computers.

BASIC CONCEPTS:
- Variables: Store data values
- Functions: Reusable code blocks
- Loops: Repeat actions
- Conditionals: Make decisions

EXAMPLE CODE:
print("Hello, World!")
x = 10
if x > 5:
    print("x is greater than 5")

CAREER PATHS:
1. Software Development
2. Data Science
3. Cybersecurity
4. AI Engineering"""
        }
        
        for filename, content in samples.items():
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"  ✅ Created: {filename}")
    
    def search(self, question, max_results=3):
        """Search for relevant content"""
        if not self.loaded:
            return []
        
        question_lower = question.lower()
        results = []
        
        for item in self.data:
            content_lower = item['content'].lower()
            score = 0
            
            # Simple relevance scoring
            for word in question_lower.split():
                if len(word) > 3:  # Only meaningful words
                    if word in content_lower:
                        score += 2
                    elif any(word in cw for cw in content_lower.split()):
                        score += 1
            
            if score > 0:
                results.append({
                    'score': score,
                    'content': item['content'],
                    'source': item['source'],
                    'section': item['section_id']
                })
        
        # Sort by score and return top results
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:max_results]
    
    def answer_question(self, question):
        """Answer a question using the knowledge base"""
        print(f"\n🤔 Question: {question}")
        
        results = self.search(question)
        
        if not results:
            return {
                'answer': "I couldn't find specific information about this in the course materials. Try asking about biology or computer science topics.",
                'sources': [],
                'confidence': 'low'
            }
        
        # Build context from results
        context = "\n".join([r['content'] for r in results])
        
        # Generate answer based on context
        answer = self._generate_answer(question, context)
        
        return {
            'answer': answer,
            'sources': [{'source': r['source'], 'section': r['section']} for r in results],
            'confidence': 'high' if len(results) > 0 else 'medium'
        }
    
    def _generate_answer(self, question, context):
        """Generate answer from context"""
        question_lower = question.lower()
        
        # Extract key topic
        if 'biology' in question_lower:
            topic = 'biology'
        elif 'programming' in question_lower or 'computer' in question_lower or 'code' in question_lower:
            topic = 'computer science'
        elif 'photosynthesis' in question_lower:
            topic = 'photosynthesis'
        elif 'cell' in question_lower:
            topic = 'cells'
        else:
            topic = 'general'
        
        # Find the most relevant sentence from context
        sentences = [s.strip() for s in context.replace('\n', '. ').split('.') if s.strip()]
        
        if sentences:
            # Try to find a sentence that directly answers the question
            for sentence in sentences:
                sentence_lower = sentence.lower()
                question_words = [w for w in question_lower.split() if len(w) > 3]
                
                if any(word in sentence_lower for word in ['is the', 'are the', 'means', 'defined as']):
                    if any(qw in sentence_lower for qw in question_words):
                        return f"According to the course materials: {sentence}"
            
            # Return the first meaningful sentence
            for sentence in sentences:
                if len(sentence) > 20 and len(sentence) < 150:
                    return f"Based on the course materials: {sentence}"
        
        # Fallback answers by topic
        answers = {
            'biology': "Biology is the scientific study of life and living organisms, including their structure, function, growth, and evolution.",
            'computer science': "Computer Science involves the study of computers and computational systems, including programming, algorithms, and data structures.",
            'photosynthesis': "Photosynthesis is the process by which plants convert light energy into chemical energy to produce food.",
            'cells': "Cells are the basic structural and functional units of all living organisms.",
            'general': f"Based on the course materials, '{question}' is an important topic covered in your studies."
        }
        
        return answers.get(topic, answers['general'])

def main():
    """Main interactive session"""
    # Initialize knowledge base
    kb = KnowledgeBase()
    kb.load_courses()
    
    print("\n" + "=" * 40)
    print("💬 INTERACTIVE Q&A SESSION")
    print("=" * 40)
    print("\n💡 Try questions like:")
    print("  • What is biology?")
    print("  • Explain programming")
    print("  • Tell me about cells")
    print("  • Type 'quit' to exit")
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
            result = kb.answer_question(question)
            
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

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("\n🧪 Running quick test...")
        kb = KnowledgeBase()
        kb.load_courses()
        
        test_questions = [
            "What is biology?",
            "Explain programming",
            "What are cells?"
        ]
        
        for q in test_questions:
            result = kb.answer_question(q)
            print(f"\nQ: {q}")
            print(f"A: {result['answer'][:80]}...")
            print(f"Sources: {len(result['sources'])}")
        
        print("\n✅ Test complete! Run without arguments for interactive mode.")
    else:
        main()
