"""
Simple embeddings for educational content
"""
import numpy as np

class SimpleEmbeddings:
    """Simple embedding model for testing"""
    
    def __init__(self):
        print("🤖 Using simple embeddings for testing")
        self.dimension = 384  # Common embedding dimension
    
    def embed_text(self, text):
        """Create simple deterministic embedding"""
        # Create deterministic "embeddings" based on text hash
        import hashlib
        text_hash = int(hashlib.md5(text.encode()).hexdigest()[:8], 16)
        
        # Create deterministic vector
        np.random.seed(text_hash)
        embedding = np.random.randn(self.dimension).tolist()
        
        # Normalize
        norm = np.linalg.norm(embedding)
        embedding = [e/norm for e in embedding]
        
        return embedding
    
    def embed_batch(self, texts):
        """Embed multiple texts"""
        return [self.embed_text(text) for text in texts]
    
    def get_embedding_dimension(self):
        """Get embedding dimension"""
        return self.dimension

if __name__ == "__main__":
    # Test embeddings
    embedder = SimpleEmbeddings()
    
    test_texts = [
        "Biology is the study of living organisms.",
        "Programming involves writing code."
    ]
    
    print("Testing embeddings...")
    for text in test_texts:
        emb = embedder.embed_text(text)
        print(f"Text: {text[:30]}...")
        print(f"Embedding length: {len(emb)}")
        print(f"First 3 values: {emb[:3]}")
        print()
