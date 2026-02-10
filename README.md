🎓 Educational Content Assistant
A Retrieval-Augmented Generation (RAG) system designed for educational content delivery and personalized learning.
A comprehensive RAG-based educational assistant with local AI capabilities – 100% free, no API costs!

✨ Features
🤖 AI Tutor
Ask any educational question

Local Ollama integration (Gemma:2b, Qwen models)

Multiple answer styles & difficulty levels

100% private – all processing on your device

📄 PDF Summarizer
Upload and extract text from PDFs

AI-powered summaries with focus control

Support for academic papers, textbooks, notes

❓ Quiz Generator
Create quizzes on any topic

Multiple choice, true/false, short answer

Adjustable difficulty (Easy/Medium/Hard)

Interactive quiz interface

🔍 Course Search
Semantic search through course materials

Sample courses: Biology & Computer Science

Relevance scoring and source tracking

Expandable results for detailed viewing

🚀 Quick Start (5-Minute Setup)
Prerequisites
Python 3.9+

Git

Ollama (for local AI)

Step 1: Clone & Setup
git clone https://github.com/VyshnaviER/educational-content-assistant.git
cd educational-content-assistant
pip install -r requirements.txt

Step 2: Install Ollama (Local AI Engine)
# Download from: https://ollama.com/download
# Then verify installation:
ollama --version  # Should show version number

Step 3: Launch AI Services
# TERMINAL 1: Start Ollama (keep running!)
ollama serve

# TERMINAL 2: Download AI model
ollama pull gemma:2b

Step 4: Start Application
# TERMINAL 3: Launch the web app
streamlit run src/streamlit_app.py

Step 5: Access Dashboard
Open your browser to: http://localhost:8501

📖 Try Sample Courses
The project includes pre-loaded educational content:

<img width="638" height="199" alt="image" src="https://github.com/user-attachments/assets/6b5d5217-59cc-4a98-85fe-dc560ef6b223" />

