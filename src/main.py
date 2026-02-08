#!/usr/bin/env python3
"""
Educational Content Assistant - Main Entry Point
"""
import os
import sys
import argparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def run_cli():
    """Run command line interface"""
    from app.cli import main as cli_main
    cli_main()

def run_document_processor():
    """Run document processor"""
    from document_processor.main import process_documents
    process_documents()

def run_generation_test():
    """Test generation system"""
    from generation.main import test_generation_system
    test_generation_system()

def run_web_ui():
    """Run web UI"""
    try:
        import streamlit
        # Streamlit will be run from command line
        print("Run: streamlit run src/app/ui.py")
    except ImportError:
        print("Streamlit not installed. Run: pip install streamlit")

def main():
    parser = argparse.ArgumentParser(description="Educational Content Assistant")
    parser.add_argument("--mode", choices=["cli", "process", "test", "web", "all"],
                       default="cli", help="Run mode")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🎓 EDUCATIONAL CONTENT ASSISTANT")
    print("=" * 60)
    
    # Check environment
    if os.path.exists('.env'):
        print("✅ Environment variables loaded")
    else:
        print("⚠️  No .env file found. Using default settings.")
        print("   Copy .env.example to .env for API keys")
    
    if args.mode == "cli":
        run_cli()
    elif args.mode == "process":
        run_document_processor()
    elif args.mode == "test":
        run_generation_test()
    elif args.mode == "web":
        run_web_ui()
    elif args.mode == "all":
        print("\nRunning complete system test...")
        run_document_processor()
        print("\n" + "="*40)
        run_generation_test()
        print("\n" + "="*40)
        print("\nTo use CLI: python src/main.py --mode cli")
        print("To launch web UI: streamlit run src/app/ui.py")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
