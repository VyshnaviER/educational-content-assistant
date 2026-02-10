# Educational Content Assistant
A Retrieval-Augmented Generation (RAG) system designed for educational content delivery and personalized learning.
A comprehensive RAG-based educational assistant with local AI capabilities – 100% free, no API costs!

## Features
## AI Tutor
Ask any educational question

Local Ollama integration (Gemma:2b, Qwen models)

Multiple answer styles & difficulty levels

100% private – all processing on your device

## PDF Summarizer
Upload and extract text from PDFs

AI-powered summaries with focus control

Support for academic papers, textbooks, notes

## Quiz Generator
Create quizzes on any topic

Multiple choice, true/false, short answer

Adjustable difficulty (Easy/Medium/Hard)

Interactive quiz interface

## Course Search
Semantic search through course materials

Sample courses: Biology & Computer Science

Relevance scoring and source tracking

Expandable results for detailed viewing

# Quick Start (5-Minute Setup)
## Prerequisites
Python 3.9+
Git
Ollama (for local AI)

### Step 1: Clone & Setup
git clone https://github.com/VyshnaviER/educational-content-assistant.git
cd educational-content-assistant
pip install -r requirements.txt

### Step 2: Install Ollama (Local AI Engine)

 Download from: https://ollama.com/download
### Then verify installation:
ollama --version  # Should show version number

### Step 3: Launch AI Services
TERMINAL 1: Start Ollama (keep running!)
ollama serve

TERMINAL 2: Download AI model
ollama pull gemma:2b

### Step 4: Start Application
TERMINAL 3: Launch the web app
streamlit run src/streamlit_app.py

### Step 5: Access Dashboard
Open your browser to: http://localhost:8501

### Try Sample Courses
The project includes pre-loaded educational content:

<img width="638" height="199" alt="image" src="https://github.com/user-attachments/assets/6b5d5217-59cc-4a98-85fe-dc560ef6b223" />

## Project Architecture
<img width="573" height="356" alt="image" src="https://github.com/user-attachments/assets/cbd9aad4-3d93-420e-b0d8-c54fb8cbbaf6" />


## Configuration
### Local AI Setup
#### Verify Ollama is running (in a separate terminal)
curl http://localhost:11434/api/tags

#### Expected response:
#### {"models":[{"name":"gemma:2b","modified_at":"2024-..."}]}

## Optional: Alternative Models
### Smaller, faster model (less capable)
ollama pull qwen2.5:0.5b

### Larger, more capable model (requires more RAM)
ollama pull llama2:7b

## Using the Application
### Web Dashboard (http://localhost:8501)
1.AI Tutor: Select from sidebar → Ask question → Choose difficulty

2.PDF Summarizer: Upload PDF → Adjust focus → Get summary

3.Quiz Generator: Enter topic → Select format → Take quiz

4.Course Search: Type keywords → Browse results → Expand details

### Quick Testing
. Try AI Tutor: Ask "Explain photosynthesis in simple terms"

. Test Quiz Generator: Topic "Python basics", 5 questions

. Explore Course Search: Search "neural networks" in Computer Science

## Troubleshooting
### Issue: AI Tutor shows "Not running" or requires Ollama
Solution: Ensure ollama serve is running in a separate terminal before starting the app.

### Issue: "Model not found" error
Solution: Verify the model is downloaded:
ollama list  # Should show "gemma:2b"

### Issue: App starts but AI features don't work
Solution: Check Ollama is accessible:
curl http://localhost:11434/api/tags  # Should return model list

### Issue: Slow responses from AI Tutor
Solution: Try a smaller model:
ollama pull qwen2.5:0.5b  # Faster but less capable

### Issue: Port 8501 already in use
Solution: Run Streamlit on a different port:
streamlit run src/streamlit_app.py --server.port 8502


## Verification Checklist
. ollama serve running in Terminal 1

. gemma:2b appears in ollama list

. curl http://localhost:11434/api/tags returns model list

. Streamlit app loads without errors

. AI Status shows "✅ Running"

## Deployment Options
### Option 1: Local Development (Recommended)
Complete local setup (as above)
Best for: Privacy, no internet required, free

### Option 2: Cloud Adaptation (Future)
Replace Ollama with cloud APIs
Add OPENAI_API_KEY or ANTHROPIC_API_KEY to .env
Modify llm_manager.py to use cloud endpoints


## Testing the System
### Basic Functionality Tes
1. Start all services
   Terminal 1: ollama serve
   Terminal 2: streamlit run src/streamlit_app.py

2. Test each feature
    - AI Tutor: Simple question → Should get response
    - PDF Summarizer: Upload sample PDF → Should generate summary
    - Quiz Generator: Enter "Biology" → Should create quiz
    - Course Search: Search "cell" → Should show biology content

3. Verify all components work

## Performance Expectations
 . AI Responses: 2-10 seconds (depends on model & hardware)

 . PDF Processing: 5-30 seconds (depends on file size)

 . Quiz Generation: 3-8 seconds

 . Course Search: Instant

 ## Contributing
### Areas for Improvement
 . Additional educational content (Physics, Chemistry, History)

 . More AI model options (Llama, Mistral, Phi)

 . Mobile-responsive UI enhancements

 . Export features (save quizzes, share summaries)

 . Integration with learning management systems

 . Multi-language support

## Development Setup
### 1. Fork and clone repository
### 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

### 3. Install dev dependencies
pip install -r requirements.txt

### 4. Make changes and test
#### 5. Submit pull request

## Support
Live App: http://localhost:8501 (when running)

### Common Questions
Q: Why do I need Ollama?
A: This app uses 100% local AI for privacy and zero API costs.

Q: Can I use cloud AI instead?
A: Currently optimized for local use. Cloud adaptation requires code changes.

Q: What are the system requirements?
A: 8GB RAM minimum, 16GB recommended for best AI performance.

## Acknowledgments
Built with amazing open-source tools:

. Streamlit - Web application framework

. Ollama - Local LLM runner

. LangChain - RAG pipeline orchestration

. Sentence-Transformers - Semantic search embeddings





##Happy Learning! 🎓
### Empowering education with local AI - no subscriptions, no limits, complete privacy.
