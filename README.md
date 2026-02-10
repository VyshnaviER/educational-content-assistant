# 🎓 Educational Content Assistant

A comprehensive RAG-based educational assistant with **local AI capabilities** - 100% free, no API costs!

## ✨ Features

### 🤖 **AI Tutor**
- Ask any educational question
- Local Ollama integration (Gemma:2b, Qwen models)
- Multiple answer styles & difficulty levels
- 100% private - all processing on your device

### 📄 **PDF Summarizer**  
- Upload and extract text from PDFs
- AI-powered summaries with focus control
- Support for academic papers, textbooks, notes

### ❓ **Quiz Generator**
- Create quizzes on any topic
- Multiple choice, true/false, short answer
- Adjustable difficulty (Easy/Medium/Hard)
- Interactive quiz interface

### 🔍 **Course Search**
- Semantic search through course materials
- Sample courses: Biology & Computer Science
- Relevance scoring and source tracking
- Expandable results for detailed viewing

## 🚀 Quick Start

```bash
# 1. Clone & setup
git clone https://github.com/VyshnaviER/educational-content-assistant.git
cd educational-content-assistant
pip install -r requirements.txt

# 2. Install Ollama (local AI)
# Download from https://ollama.com/

# 3. Pull AI model
ollama pull gemma:2b

# 4. Run Ollama in separate terminal:
ollama serve

# 5. Start the app
streamlit run src/streamlit_app.py
