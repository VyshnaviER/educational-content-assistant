"""
Smart chunking for educational content
Preserves context and structure
"""
import re
from typing import List, Dict, Any

class EducationalChunker:
    """Intelligent chunking for educational materials"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.section_patterns = [
            r'^(Chapter \d+[:.]?\s*.+)$',
            r'^(Section \d+[:.]?\s*.+)$',
            r'^(Unit \d+[:.]?\s*.+)$',
            r'^(Lecture \d+[:.]?\s*.+)$',
            r'^(Topic \d+[:.]?\s*.+)$',
            r'^(\d+\.\d+\s+.+)$',  # 1.1 Introduction
            r'^(\d+\.\s+.+)$',     # 1. Introduction
        ]
    
    def _split_by_sections(self, text: str) -> List[str]:
        """Split text by educational section markers"""
        lines = text.split('\n')
        sections = []
        current_section = []
        
        for line in lines:
            line_stripped = line.strip()
            is_section_header = any(
                re.match(pattern, line_stripped, re.IGNORECASE) 
                for pattern in self.section_patterns
            )
            
            if is_section_header and current_section:
                sections.append('\n'.join(current_section))
                current_section = [line_stripped]
            else:
                if line_stripped or current_section:  # Keep non-empty lines
                    current_section.append(line_stripped)
        
        if current_section:
            sections.append('\n'.join(current_section))
        
        return sections
    
    def _split_by_sentences(self, text: str) -> List[str]:
        """Split text by sentences while preserving educational context"""
        # Educational sentence splitting - preserve equations, definitions
        sentence_enders = r'(?<=[.!?])\s+(?=[A-Z])'
        sentences = re.split(sentence_enders, text)
        return [s.strip() for s in sentences if s.strip()]
    
    def chunk_document(self, document: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Chunk a single document into educational chunks"""
        content = document['content']
        metadata = document['metadata']
        
        # First split by sections
        sections = self._split_by_sections(content)
        
        chunks = []
        chunk_id = 0
        
        for section in sections:
            if len(section) <= self.chunk_size:
                # Section fits in one chunk
                chunk_metadata = metadata.copy()
                chunk_metadata.update({
                    'chunk_id': chunk_id,
                    'section': section.split('\n')[0][:100] if section else '',
                    'chunk_size': len(section)
                })
                chunks.append({
                    'content': section,
                    'metadata': chunk_metadata
                })
                chunk_id += 1
            else:
                # Split section into smaller chunks
                words = section.split()
                for i in range(0, len(words), self.chunk_size - self.chunk_overlap):
                    chunk_words = words[i:i + self.chunk_size]
                    chunk_text = ' '.join(chunk_words)
                    
                    chunk_metadata = metadata.copy()
                    chunk_metadata.update({
                        'chunk_id': chunk_id,
                        'section': section.split('\n')[0][:100] if section else '',
                        'chunk_part': f"{i//self.chunk_size + 1}",
                        'chunk_size': len(chunk_text)
                    })
                    
                    chunks.append({
                        'content': chunk_text,
                        'metadata': chunk_metadata
                    })
                    chunk_id += 1
        
        print(f"📝 Created {len(chunks)} chunks from document")
        return chunks
    
    def chunk_documents(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Chunk multiple documents"""
        all_chunks = []
        for doc in documents:
            chunks = self.chunk_document(doc)
            all_chunks.extend(chunks)
        
        print(f"📊 Total chunks created: {len(all_chunks)}")
        return all_chunks

if __name__ == "__main__":
    # Test chunker
    chunker = EducationalChunker(chunk_size=500, chunk_overlap=100)
    
    test_doc = {
        'content': """Chapter 1: Introduction to Biology
    
    Biology is the study of living organisms. It encompasses various sub-disciplines.
    
    Section 1.1: Cell Theory
    
    All living things are composed of cells. Cells are the basic unit of life.
    
    Section 1.2: Evolution
    
    Species change over time through natural selection.""",
        'metadata': {'source': 'test.pdf', 'page': 1, 'type': 'pdf'}
    }
    
    chunks = chunker.chunk_document(test_doc)
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} ---")
        print(chunk['content'][:200] + "...")
        print(f"Metadata: {chunk['metadata']}")
