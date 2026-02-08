"""
Main document processing pipeline
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from document_processor.loader import EducationalDocumentLoader
from document_processor.chunker import EducationalChunker
import json

def process_course_materials(input_dir: str = "data/sample_courses", 
                           output_dir: str = "data/processed"):
    """Main processing pipeline"""
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 60)
    print("📚 EDUCATIONAL DOCUMENT PROCESSING PIPELINE")
    print("=" * 60)
    
    # Step 1: Load documents
    print("\n1. 📥 Loading documents...")
    loader = EducationalDocumentLoader()
    documents = loader.load_documents(input_dir)
    
    if not documents:
        print("❌ No documents found. Please add files to data/sample_courses/")
        print("   Supported formats: PDF, DOCX, TXT, PPTX")
        return
    
    # Step 2: Chunk documents
    print("\n2. ✂️  Chunking documents...")
    chunker = EducationalChunker(chunk_size=1000, chunk_overlap=200)
    chunks = chunker.chunk_documents(documents)
    
    # Step 3: Save processed chunks
    print("\n3. 💾 Saving processed data...")
    
    # Save as JSON
    output_file = os.path.join(output_dir, "processed_chunks.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)
    
    # Save summary
    summary_file = os.path.join(output_dir, "processing_summary.txt")
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(f"Processing Summary\n")
        f.write(f"{'='*40}\n")
        f.write(f"Input Directory: {input_dir}\n")
        f.write(f"Documents Loaded: {len(documents)}\n")
        f.write(f"Total Chunks Created: {len(chunks)}\n")
        f.write(f"Output Files: {output_file}, {summary_file}\n")
    
    print(f"\n✅ Processing complete!")
    print(f"   📄 Documents: {len(documents)}")
    print(f"   🧩 Chunks: {len(chunks)}")
    print(f"   💾 Saved to: {output_file}")
    print(f"   📊 Summary: {summary_file}")
    
    return chunks

if __name__ == "__main__":
    # Create sample directory if it doesn't exist
    sample_dir = "data/sample_courses"
    os.makedirs(sample_dir, exist_ok=True)
    
    # Check if sample directory is empty
    if not os.listdir(sample_dir):
        print("ℹ️  Sample directory is empty. Creating sample educational content...")
        
        # Create a sample biology text
        sample_content = """Introduction to Biology - Sample Chapter

Chapter 1: The Science of Life

Biology is the scientific study of life and living organisms. It explores the structure, function, growth, origin, evolution, and distribution of living things.

Section 1.1: Characteristics of Life

All living organisms share certain characteristics:
1. Cellular organization
2. Reproduction
3. Metabolism
4. Homeostasis
5. Heredity
6. Response to stimuli
7. Growth and development
8. Adaptation through evolution

Section 1.2: Levels of Biological Organization

Life can be studied at different levels:
- Molecular level (DNA, proteins)
- Cellular level (cells, organelles)
- Tissue level (groups of similar cells)
- Organ level (heart, liver, brain)
- Organ system level (digestive system)
- Organism level (individual living thing)
- Population level (group of same species)
- Ecosystem level (community + environment)
- Biosphere level (all ecosystems on Earth)

Key Concepts:
- Photosynthesis: Process by which plants convert light energy to chemical energy
- Cellular respiration: Process by which cells convert nutrients into ATP
- DNA: Deoxyribonucleic acid, the hereditary material
- Evolution: Change in heritable characteristics of biological populations

This sample content demonstrates how the Educational Assistant processes and retrieves information from course materials."""
        
        sample_file = os.path.join(sample_dir, "biology_sample.txt")
        with open(sample_file, 'w', encoding='utf-8') as f:
            f.write(sample_content)
        print(f"✅ Created sample file: {sample_file}")
    
    # Run processing pipeline
    chunks = process_course_materials()
    
    # Display sample chunk
    if chunks:
        print(f"\n📖 Sample Chunk (1 of {len(chunks)}):")
        print("-" * 40)
        print(chunks[0]['content'][:300] + "...")
        print(f"\n📋 Metadata:")
        for key, value in chunks[0]['metadata'].items():
            print(f"  {key}: {value}")
