"""
ChromaDB vector store management
"""
import os
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any
import uuid
import json

class EducationalVectorStore:
    """Manages vector database for educational content"""
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        """
        Initialize ChromaDB vector store
        
        Args:
            persist_directory: Directory to persist database
        """
        self.persist_directory = persist_directory
        os.makedirs(persist_directory, exist_ok=True)
        
        # Initialize Chroma client
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(anonymized_telemetry=False)
        )
        
        print(f"✅ Vector store initialized at: {persist_directory}")
    
    def create_collection(self, collection_name: str = "educational_content"):
        """Create or get a collection"""
        try:
            self.collection = self.client.get_or_create_collection(
                name=collection_name,
                metadata={"description": "Educational course materials"}
            )
            print(f"✅ Collection '{collection_name}' ready")
            return self.collection
        except Exception as e:
            print(f"❌ Error creating collection: {e}")
            raise
    
    def add_documents(self, chunks: List[Dict[str, Any]], 
                     embeddings: List[List[float]] = None):
        """
        Add documents to vector store
        
        Args:
            chunks: List of chunk dictionaries with content and metadata
            embeddings: Optional pre-computed embeddings
        """
        if not hasattr(self, 'collection'):
            self.create_collection()
        
        print(f"📥 Adding {len(chunks)} documents to vector store...")
        
        # Prepare data for ChromaDB
        ids = []
        documents = []
        metadatas = []
        
        for i, chunk in enumerate(chunks):
            chunk_id = str(uuid.uuid4())
            ids.append(chunk_id)
            documents.append(chunk['content'])
            
            # Prepare metadata
            metadata = chunk['metadata'].copy()
            metadata['chunk_index'] = i
            metadata['length'] = len(chunk['content'])
            metadatas.append(metadata)
        
        # Add to collection
        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings  # Can be None, Chroma will compute
        )
        
        print(f"✅ Added {len(chunks)} documents to vector store")
        
        # Show collection info
        count = self.collection.count()
        print(f"📊 Total documents in collection: {count}")
    
    def search(self, query: str, n_results: int = 5, 
               where_filter: Dict = None) -> List[Dict[str, Any]]:
        """
        Search for similar documents
        
        Args:
            query: Search query
            n_results: Number of results to return
            where_filter: Metadata filter (e.g., {"course": "biology"})
        
        Returns:
            List of search results with documents and metadata
        """
        if not hasattr(self, 'collection'):
            self.create_collection()
        
        print(f"🔍 Searching for: '{query}'")
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_filter,
            include=["documents", "metadatas", "distances"]
        )
        
        # Format results
        formatted_results = []
        if results['documents']:
            for i in range(len(results['documents'][0])):
                formatted_results.append({
                    'content': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'distance': results['distances'][0][i]
                })
        
        print(f"📄 Found {len(formatted_results)} relevant documents")
        return formatted_results
    
    def get_collection_info(self):
        """Get information about the collection"""
        if not hasattr(self, 'collection'):
            self.create_collection()
        
        count = self.collection.count()
        return {
            'collection_name': self.collection.name,
            'document_count': count,
            'persist_directory': self.persist_directory
        }
    
    def delete_collection(self, collection_name: str = None):
        """Delete a collection"""
        try:
            if collection_name:
                self.client.delete_collection(collection_name)
                print(f"🗑️  Deleted collection: {collection_name}")
            elif hasattr(self, 'collection'):
                self.client.delete_collection(self.collection.name)
                print(f"🗑️  Deleted current collection")
        except Exception as e:
            print(f"❌ Error deleting collection: {e}")

if __name__ == "__main__":
    # Test vector store
    print("🧪 Testing vector store...")
    
    # Initialize
    vector_store = EducationalVectorStore()
    
    # Create test documents
    test_chunks = [
        {
            'content': "Biology is the scientific study of life and living organisms.",
            'metadata': {'course': 'biology', 'topic': 'introduction', 'page': 1}
        },
        {
            'content': "Photosynthesis is the process plants use to convert sunlight into energy.",
            'metadata': {'course': 'biology', 'topic': 'photosynthesis', 'page': 45}
        },
        {
            'content': "Newton's laws of motion describe the relationship between motion and forces.",
            'metadata': {'course': 'physics', 'topic': 'mechanics', 'page': 23}
        }
    ]
    
    # Add to vector store
    vector_store.add_documents(test_chunks)
    
    # Test search
    results = vector_store.search("What is biology?", n_results=2)
    print(f"\n🔍 Search results for 'What is biology?':")
    for i, result in enumerate(results):
        print(f"\nResult {i+1}:")
        print(f"Content: {result['content']}")
        print(f"Metadata: {result['metadata']}")
        print(f"Distance: {result['distance']:.4f}")
    
    # Get info
    info = vector_store.get_collection_info()
    print(f"\n📊 Collection info: {info}")
