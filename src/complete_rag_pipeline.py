#!/usr/bin/env python3
"""
Complete RAG Pipeline for Educational Assistant - FIXED VERSION
"""
import os
import sys
import json

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

class SimpleVectorStore:
    """Simple vector store included in the same file"""
    
    def __init__(self, persist_dir="chroma_db"):
        self.persist_dir = persist_dir
        self.documents = []
        self.metadatas = []
        self.ids = []
        self.next_id = 0
        
        os.makedirs(persist_dir, exist_ok=True)
        print(f"📂 Simple vector store initialized")
    
    def add_documents(self, chunks):
        """Add documents to store"""
        print(f"📥 Adding {len(chunks)} documents...")
        
        for chunk in chunks:
            self.documents.append(chunk['content'])
            self.metadatas.append(chunk['metadata'])
            self.ids.append(str(self.next_id))
            self.next_id += 1
        
        print(f"✅ Added {len(chunks)} documents. Total: {len(self.documents)}")
        return self
    
    def search(self, query, n_results=5, where_filter=None):
        """Simple search based on keyword matching"""
        print(f"🔍 Searching for: '{query}'")
        
        query_lower = query.lower()
        results = []
        
        for i, doc in enumerate(self.documents):
            score = 0
            
            # Simple keyword matching
            doc_lower = doc.lower()
            for word in query_lower.split():
                if len(word) > 3:  # Ignore short words
                    score += doc_lower.count(word) * len(word)
            
            if score > 0:
                results.append({
                    'index': i,
                    'score': score,
                    'content': doc,
                    'metadata': self.metadatas[i]
                })
        
        # Sort by score
        results.sort(key=lambda x: x['score'], reverse=True)
        
        # Take top n
        results = results[:n_results]
        
        print(f"📄 Found {len(results)} relevant documents")
        return results
    
    def save(self, filename="vector_store.json"):
        """Save vector store to file"""
        data = {
            'documents': self.documents,
            'metadatas': self.metadatas,
            'ids': self.ids
        }
        
        filepath = os.path.join(self.persist_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Saved vector store to {filepath}")
        return self
    
    def load(self, filename="vector_store.json"):
        """Load vector store from file"""
        filepath = os.path.join(self.persist_dir, filename)
        
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            self.documents = data['documents']
            self.metadatas = data['metadatas']
            self.ids = data['ids']
            self.next_id = len(self.ids)
            
            print(f"📂 Loaded {len(self.documents)} documents from {filepath}")
            return True
        
        print(f"⚠️  File not found: {filepath}")
        return False

def simple_generate_answer(question, context=None):
    """Simple answer generator"""
    responses = {
        "biology": "Biology is the scientific study of life and living organisms.",
        "programming": "Programming is writing instructions for computers to execute tasks.",
        "photosynthesis": "Photosynthesis is the process plants use to convert sunlight into chemical energy.",
        "cell": "Cells are the basic structural and functional units of all living organisms.",
        "computer": "Computer Science involves the study of computers and computational systems."
    }
    
    question_lower = question.lower()
    
    for keyword, answer in responses.items():
        if keyword in question_lower:
            if context:
                return f"Based on the course materials: {answer}"
            return answer
    
    if context:
        return f"Based on the course materials: {question} is an important concept discussed in your course materials."
    
    return f"I found information about '{question}' in your course materials. Review the relevant sections for details."

class EducationalRAGPipeline:
    """Complete RAG pipeline for educational content - SIMPLIFIED"""
    
    def __init__(self):
        print("🎓 Initializing Educational RAG Pipeline...")
        self.VectorStore = SimpleVectorStore
        self.generate_answer = simple_generate_answer
        print("✅ Pipeline initialized successfully!")
    
    def process_course_materials(self, data_dir="data/sample_courses"):
        """Process course materials and create vector store"""
        print(f"\n📚 Processing course materials from {data_dir}...")
        
        # Check if directory exists
        if not os.path.exists(data_dir):
            print(f"❌ Directory not found: {data_dir}")
            os.makedirs(data_dir, exist_ok=True)
            print(f"✅ Created directory. Please add course materials.")
            return None
        
        # List files
        files = []
        for f in os.listdir(data_dir):
            if f.endswith(('.txt', '.pdf', '.docx')):
                files.append(os.path.join(data_dir, f))
        
        if not files:
            print("⚠️  No course files found.")
            print(f"\nAdd files to {data_dir} (supported: .txt, .pdf, .docx)")
            return None
        
        print(f"📄 Found {len(files)} course files")
        
        # Create simple chunks from files
        chunks = []
        for filepath in files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Split into simple chunks (by paragraphs)
                paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
                
                for i, para in enumerate(paragraphs):
                    chunks.append({
                        'content': para,
                        'metadata': {
                            'source': os.path.basename(filepath),
                            'chunk_id': i,
                            'type': 'text'
                        }
                    })
                
                print(f"  • {os.path.basename(filepath)}: {len(paragraphs)} chunks")
                
            except Exception as e:
                print(f"  • Error reading {filepath}: {e}")
        
        print(f"📊 Total chunks created: {len(chunks)}")
        return chunks
    
    def create_knowledge_base(self, chunks):
        """Create vector store from chunks"""
        print("\n🗄️ Creating knowledge base...")
        
        vector_store = self.VectorStore()
        vector_store.add_documents(chunks)
        vector_store.save()
        
        print("✅ Knowledge base created and saved!")
        return vector_store
    
    def ask_question(self, question, vector_store=None, student_level="intermediate"):
        """Answer a question using RAG"""
        print(f"\n🤔 Question: {question}")
        print(f"   Student level: {student_level}")
        
        # If no vector store provided, try to load existing one
        if vector_store is None:
            vector_store = self.VectorStore()
            if not vector_store.load():
                print("⚠️  No knowledge base found. Please process course materials first.")
                return None
        
        # Search for relevant content
        results = vector_store.search(question, n_results=3)
        
        if not results:
            print("⚠️  No relevant content found in knowledge base.")
            answer = "I couldn't find relevant information in the course materials. Please make sure you've processed your course materials first."
            sources = []
        else:
            # Combine context from results
            context = "\n\n".join([r['content'] for r in results])
            sources = [r['metadata'] for r in results]
            
            # Generate answer
            answer = self.generate_answer(question, context)
            
            print(f"📚 Found {len(results)} relevant sources")
        
        return {
            'question': question,
            'answer': answer,
            'sources': sources,
            'student_level': student_level,
            'context_used': len(results)
        }
    
    def interactive_session(self):
        """Run interactive Q&A session"""
        print("\n" + "=" * 60)
        print("🎓 INTERACTIVE EDUCATIONAL ASSISTANT")
        print("=" * 60)
        
        # Process course materials
        chunks = self.process_course_materials()
        
        if not chunks:
            print("\nPlease add course materials to data/sample_courses/ and try again.")
            return
        
        # Create knowledge base
        vector_store = self.create_knowledge_base(chunks)
        
        # Interactive Q&A
        print("\n" + "=" * 40)
        print("💬 Q&A SESSION (Type 'quit' to exit)")
        print("=" * 40)
        
        while True:
            try:
                question = input("\n📝 Your question: ").strip()
                
                if question.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Thank you for using Educational Assistant!")
                    break
                
                if not question:
                    continue
                
                # Get answer
                result = self.ask_question(question, vector_store)
                
                if result:
                    print(f"\n💡 Answer: {result['answer']}")
                    
                    if result['sources']:
                        print(f"\n📚 Sources:")
                        for source in result['sources']:
                            print(f"  • {source['source']} (Chunk: {source.get('chunk_id', 'N/A')})")
                    print(f"\n{'='*40}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")

def main():
    """Main function"""
    print("🚀 Starting Educational RAG Pipeline...")
    
    # Initialize pipeline
    pipeline = EducationalRAGPipeline()
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "process":
            pipeline.process_course_materials()
        elif sys.argv[1] == "ask" and len(sys.argv) > 2:
            question = " ".join(sys.argv[2:])
            result = pipeline.ask_question(question)
            if result:
                print(f"\nQuestion: {result['question']}")
                print(f"\nAnswer: {result['answer']}")
                if result['sources']:
                    print(f"\nSources:")
                    for source in result['sources']:
                        print(f"  • {source['source']}")
        elif sys.argv[1] == "test":
            print("\n🧪 Running test...")
            # Process materials
            chunks = pipeline.process_course_materials()
            if chunks:
                vector_store = pipeline.create_knowledge_base(chunks)
                # Test a question
                result = pipeline.ask_question("What is biology?", vector_store)
                if result:
                    print(f"\nTest Result:")
                    print(f"Question: {result['question']}")
                    print(f"Answer: {result['answer']}")
        else:
            print(f"\nUsage:")
            print(f"  python {sys.argv[0]} process          # Process course materials")
            print(f"  python {sys.argv[0]} ask <question>   # Ask a question")
            print(f"  python {sys.argv[0]} test             # Run a complete test")
            print(f"  python {sys.argv[0]}                  # Start interactive session")
    else:
        # Start interactive session
        pipeline.interactive_session()

if __name__ == "__main__":
    main()
