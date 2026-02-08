"""
Simple vector store for testing without ChromaDB dependencies
"""
import json
import os
from typing import List, Dict, Any
import numpy as np

class SimpleVectorStore:
    """Simple in-memory vector store for testing"""
    
    def __init__(self, persist_dir="chroma_db"):
        self.persist_dir = persist_dir
        self.documents = []
        self.embeddings = []
        self.metadatas = []
        self.ids = []
        self.next_id = 0
        
        os.makedirs(persist_dir, exist_ok=True)
        print(f"📂 Simple vector store initialized")
    
    def add_documents(self, chunks: List[Dict[str, Any]], embeddings=None):
        """Add documents to store"""
        print(f"📥 Adding {len(chunks)} documents...")
        
        for chunk in chunks:
            self.documents.append(chunk['content'])
            self.metadatas.append(chunk['metadata'])
            self.ids.append(str(self.next_id))
            self.next_id += 1
        
        print(f"✅ Added {len(chunks)} documents. Total: {len(self.documents)}")
    
    def search(self, query: str, n_results: int = 5, where_filter=None) -> List[Dict[str, Any]]:
        """
        Simple search based on keyword matching
        """
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
    
    def get_info(self):
        """Get information about the store"""
        return {
            'document_count': len(self.documents),
            'persist_dir': self.persist_dir,
            'store_type': 'simple_vector_store'
        }

if __name__ == "__main__":
    # Test the vector store
    print("🧪 Testing Simple Vector Store")
    print("=" * 40)
    
    store = SimpleVectorStore()
    
    # Create test documents
    test_chunks = [
        {
            'content': "Biology is the study of living organisms and life processes.",
            'metadata': {'source': 'biology.txt', 'page': 1, 'course': 'biology'}
        },
        {
            'content': "Photosynthesis converts sunlight into chemical energy in plants.",
            'metadata': {'source': 'biology.txt', 'page': 45, 'course': 'biology'}
        },
        {
            'content': "Programming involves writing instructions for computers to execute.",
            'metadata': {'source': 'cs.txt', 'page': 1, 'course': 'computer_science'}
        }
    ]
    
    # Add documents
    store.add_documents(test_chunks)
    
    # Test search
    results = store.search("What is biology?")
    
    print(f"\nSearch Results:")
    for i, result in enumerate(results):
        print(f"\n{i+1}. Score: {result['score']:.2f}")
        print(f"   Content: {result['content'][:60]}...")
        print(f"   Metadata: {result['metadata']}")
    
    # Save and test persistence
    store.save()
    
    print("\n" + "=" * 40)
    print("✅ Simple Vector Store test complete!")
