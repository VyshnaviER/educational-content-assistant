"""
Document Loader for various educational formats
"""
import os
from typing import List, Dict, Any
from pypdf import PdfReader
import docx2txt
from pptx import Presentation
import json

class EducationalDocumentLoader:
    """Loads various educational document formats"""
    
    SUPPORTED_EXTENSIONS = {
        '.pdf': 'load_pdf',
        '.docx': 'load_docx',
        '.pptx': 'load_pptx',
        '.txt': 'load_txt',
        '.json': 'load_json'
    }
    
    @staticmethod
    def load_pdf(file_path: str) -> List[Dict[str, Any]]:
        """Load PDF document with metadata"""
        documents = []
        try:
            reader = PdfReader(file_path)
            for page_num, page in enumerate(reader.pages, 1):
                text = page.extract_text()
                if text.strip():
                    documents.append({
                        'content': text,
                        'metadata': {
                            'source': file_path,
                            'page': page_num,
                            'total_pages': len(reader.pages),
                            'type': 'pdf'
                        }
                    })
            print(f"✅ Loaded {len(documents)} pages from {file_path}")
        except Exception as e:
            print(f"❌ Error loading PDF {file_path}: {e}")
        return documents
    
    @staticmethod
    def load_docx(file_path: str) -> List[Dict[str, Any]]:
        """Load DOCX document"""
        try:
            text = docx2txt.process(file_path)
            return [{
                'content': text,
                'metadata': {
                    'source': file_path,
                    'type': 'docx',
                    'sections': len(text.split('\n\n'))
                }
            }]
        except Exception as e:
            print(f"❌ Error loading DOCX {file_path}: {e}")
            return []
    
    @staticmethod
    def load_txt(file_path: str) -> List[Dict[str, Any]]:
        """Load plain text document"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            return [{
                'content': text,
                'metadata': {
                    'source': file_path,
                    'type': 'txt'
                }
            }]
        except Exception as e:
            print(f"❌ Error loading TXT {file_path}: {e}")
            return []
    
    def load_documents(self, directory: str) -> List[Dict[str, Any]]:
        """Load all documents from directory"""
        all_documents = []
        
        if not os.path.exists(directory):
            print(f"⚠️ Directory {directory} does not exist. Creating...")
            os.makedirs(directory, exist_ok=True)
            return all_documents
        
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            ext = os.path.splitext(filename)[1].lower()
            
            if ext in self.SUPPORTED_EXTENSIONS:
                print(f"📄 Processing {filename}...")
                loader_method = getattr(self, self.SUPPORTED_EXTENSIONS[ext])
                documents = loader_method(file_path)
                all_documents.extend(documents)
        
        print(f"📊 Total documents loaded: {len(all_documents)}")
        return all_documents

if __name__ == "__main__":
    # Test the loader
    loader = EducationalDocumentLoader()
    sample_dir = "data/sample_courses"
    docs = loader.load_documents(sample_dir)
    print(f"Test completed. Loaded {len(docs)} document chunks.")
