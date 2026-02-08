"""
Improved vector store with better search
"""
import json
import os
import re
from typing import List, Dict, Any

class ImprovedVectorStore:
    """Improved vector store with better search capabilities"""
    
    def __init__(self, persist_dir="chroma_db"):
        self.persist_dir = persist_dir
        self.documents = []
        self.metadatas = []
        self.ids = []
        self.next_id = 0
        
        os.makedirs(persist_dir, exist_ok=True)
        print(f"📂 Improved vector store initialized")
    
    def add_documents(self, chunks: List[Dict[str, Any]]):
        """Add documents to store"""
        print(f"📥 Adding {len(chunks)} documents...")
        
        for chunk in chunks:
            self.documents.append(chunk['content'])
            self.metadatas.append(chunk['metadata'])
            self.ids.append(str(self.next_id))
            self.next_id += 1
        
        print(f"✅ Added {len(chunks)} documents. Total: {len(self.documents)}")
        return self
    
    def _calculate_relevance(self, query: str, document: str) -> float:
        """Calculate relevance score between query and document"""
        query_words = set(re.findall(r'\b\w+\b', query.lower()))
        doc_words = set(re.findall(r'\b\w+\b', document.lower()))
        
        # Exact matches
        exact_matches = len(query_words.intersection(doc_words))
        
        # Partial matches (substring)
        partial_matches = 0
        for q_word in query_words:
            if len(q_word) > 3:  # Only consider words longer than 3 chars
                for d_word in doc_words:
                    if q_word in d_word or d_word in q_word:
                        partial_matches += 1
        
        # Calculate score
        score = (exact_matches * 2) + (partial_matches * 0.5)
        
        # Boost score if query words appear multiple times
        doc_lower = document.lower()
        for word in query_words:
            if len(word) > 3:
                score += doc_lower.count(word) * 0.1
        
        return score
    
    def search(self, query: str, n_results: int = 5, where_filter=None) -> List[Dict[str, Any]]:
        """Improved search with better relevance scoring"""
        print(f"🔍 Searching for: '{query}'")
        
        if not self.documents:
            print("⚠️  No documents in vector store")
            return []
        
        results = []
        
        for i, doc in enumerate(self.documents):
            score = self._calculate_relevance(query, doc)
            
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
        
        # Show top result score for debugging
        if results:
            print(f"   Top score: {results[0]['score']:.2f}")
        
        return results
    
    def save(self, filename="improved_vector_store.json"):
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
    
    def load(self, filename="improved_vector_store.json"):
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

if __name__ == "__main__":
    # Test the improved vector store
    print("🧪 Testing Improved Vector Store")
    print("=" * 50)
    
    store = ImprovedVectorStore()
    
    # Create test documents
    test_chunks = [
        {
            'content': "Biology is the scientific study of life and living organisms.",
            'metadata': {'source': 'biology.txt', 'page': 1}
        },
        {
            'content': "Cells are the basic structural units of all living things.",
            'metadata': {'source': 'biology.txt', 'page': 2}
        },
        {
            'content': "Programming involves writing code for computers.",
            'metadata': {'source': 'cs.txt', 'page': 1}
        }
    ]
    
    # Add documents
    store.add_documents(test_chunks)
    
    # Test searches
    test_queries = [
        "What is biology?",
        "Tell me about cells",
        "Explain programming"
    ]
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        results = store.search(query, n_results=2)
        
        for i, result in enumerate(results):
            print(f"  {i+1}. Score: {result['score']:.2f}")
            print(f"     Content: {result['content'][:50]}...")
    
    print("\n" + "=" * 50)
    print("✅ Improved Vector Store test complete!")
