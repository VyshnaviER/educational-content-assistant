#  **EDUCATIONAL CONTENT ASSISTANT**

  **(ER LEARNING ASSISTANT PROFESSIONAL PRO)**

## 

## **A Retrieval-Augmented Generation (RAG) System for Personalized Learning**

Version 2.0 | February 2026 | Author: Vyshnavi E R

## **1\. EXECUTIVE SUMMARY**

Educational Content Assistant is a privacy-first, 100% local AI-powered learning platform that transforms how students interact with educational content. Unlike cloud-based solutions that send user data to external servers and charge per API call, this application runs entirely on the user's machine—ensuring complete privacy, zero ongoing costs, and offline functionality.

| Core Capability | What It Does | Benefit |
| :---- | :---- | :---- |
|  AI Tutor | Answers questions using local LLMs | Private, free, offline tutoring |
| PDF Summarizer | Extracts key points from documents | Read less, learn more |
| Quiz Generator | Creates adaptive practice tests | Test knowledge instantly |
| Search | Finds relevant content across subjects | Stop searching, start learning |

Key Differentiators:

*  100% Local Processing – No data ever leaves your device  
*  Zero API Costs – No subscriptions, no credit cards  
*  Offline Capable – No internet required after initial setup  
*  Open Source – MIT licensed, free forever

## **2\. PROJECT OVERVIEW**

## **2.1 Problem Statement**

Traditional AI-powered educational tools suffer from three critical limitations.

| Problem | Impact |
| :---- | :---- |
| Privacy Concerns | User questions and documents are sent to cloud servers |
| Recurring Costs | API-based pricing creates ongoing expenses |
| Internet Dependency | Cannot function without connectivity |
| Black Box Models | Users have no control over AI behavior |
|  |  |

### 

### **2.2 Solution**

Educational Content Assistant solves these problems through:

| Solution | Implementation |
| :---- | :---- |
| Local-First Architecture | All AI models run on the user's device |
| Zero API Dependencies | No external services, no recurring costs |
| Offline Capability | Fully functional without internet after setup |
| Open Source | Complete transparency and user control |

### **2.3 Target Audience**

| User Group | Use Case |
| :---- | :---- |
| Students | Private AI tutor for homework help and exam preparation |
| Educators | Generate quizzes, summarize readings, prepare lesson materials |
| Researchers | Extract key insights from academic papers |
| Self-Learners | Explore new subjects with guided AI assistance |
| Privacy-Conscious Users | Learn without sending data to cloud servers |

## 

## **3\. CORE FEATURES**

### **3.1  AI Tutor**

Overview: The AI Tutor provides intelligent, context-aware answers to educational questions using locally-hosted large language models.

Key Capabilities:

| Feature | Description |
| :---- | :---- |
| Multiple Model Support | Compatible with Gemma:2b, Qwen2.5, Llama2, Mistral |
| Adjustable Difficulty | Beginner, Intermediate, Advanced levels |
| Answer Styles | Simple, Detailed, Technical, With Examples |
| Context Retention | Follow-up questions maintain conversation context |
| Zero Data Leakage | 100% local processing, no external API calls |

Example Interactions:

User: "Explain photosynthesis like I'm 10 years old"

AI: "Photosynthesis is how plants make their own food. 

     They use sunlight, water, and air to create sugar and oxygen. 

     It's like a kitchen where sunlight is the stove, 

     water is the ingredients, and sugar is the meal\!"

User: "What about cellular respiration?"

AI: "Cellular respiration is the opposite of photosynthesis. 

     It's how cells break down sugar to release energy. 

     Think of it as your body's way of 'digesting' the food plants made\!"

### **3.2 PDF Summarizer**

Overview: The PDF Summarizer extracts and condenses academic documents using AI-powered natural language processing.

**Key Capabilities:**

| Feature | Description |
| :---- | :---- |
| Multi-Format Support | PDF (.pdf) and Text (.txt) files |
| Summary Formats | Key Points, Detailed Summary, Chapter-wise, Study Guide |
| Adjustable Detail | 1 (brief) to 10 (comprehensive) |
| Focus Areas | Concepts, Examples, Formulas, Key Takeaways |
| Study Tools | Generate practice questions and flashcards |

**Performance Metrics:**

| Document Length | Processing Time | Summary Length |
| :---- | :---- | :---- |
| 1-10 pages | 5-10 seconds | 50-100 words |
| 11-30 pages | 10-20 seconds | 100-250 words |
| 31-50 pages | 20-30 seconds | 250-500 words |

### **3.3  Quiz Generator**

Overview: The Quiz Generator creates customized practice tests on any topic with instant scoring and detailed feedback.

Key Capabilities:

| Feature | Description |
| :---- | :---- |
| Question Types | Multiple Choice, True/False, Short Answer, Mixed |
| Difficulty Levels | Easy, Medium, Hard, Expert |
| Question Count | 1 to 20 questions per quiz |
| AI Generation | Automatically creates relevant, varied questions |
| Instant Feedback | Immediate scoring with answer explanations |

**Scoring System:**

| Score | Grade | Feedback |
| :---- | :---- | :---- |
| 100% | A+ | Perfect\! Excellent work\! |
| 80-99% | A/B | Good job\! Well done\! |
| 60-79% | C/D | Keep practicing\! You're getting there. |
| Below 60% | F |  Review the material and try again. |

### **3.4 Course Search**

Overview: Course Search is a semantic search engine that understands meaning—not just keywords—across structured educational content.

Available Courses:

| Course | Beginner | Intermediate | Advanced |
| :---- | :---- | :---- | :---- |
| Biology | Cells, Photosynthesis, DNA basics | Genetics, Enzymes, Mitosis | Krebs cycle, CRISPR, Epigenetics |
| Computer Science | Python, HTML, Variables, Loops | OOP, SQL, APIs, Git | ML, Neural Networks, Docker |
| Physics | Forces, Energy, Gravity | Quantum, Relativity, Thermodynamics | String theo |

## 

## **4\. SYSTEM ARCHITECTURE**

### **4.1 High-Level Architecture Diagram**

![][image1]  
![][image2]

### **4.2 AI Tutor Workflow**

![][image3]  
![][image4]

### **4.3 PDF Summarizer Workflow**

![][image5]

                                                                         

### **4.4 Quiz Generator Workflow**

![][image6]  
![][image7]

### **4.5 Course Search Workflow**

![][image8]

## **5\. TECHNOLOGY STACK**

### **5.1 Core Technologies**

| Layer | Technology | Version | Purpose |
| :---- | :---- | :---- | :---- |
| Frontend | Streamlit | 1.28+ | Web interface framework |
| AI Runtime | Ollama | 0.1+ | Local LLM execution |
| RAG Framework | LangChain | 0.1+ | Pipeline orchestration |
| Vector Store | ChromaDB | 0.4+ | Semantic search |
| Embeddings | Sentence-Transformers | 2.2+ | Text vectorization |
| PDF Processing | PyPDF2 | 3.0+ | Document text extraction |
| Environment | Python | 3.9+ | Core programming language |

### **5.3 System Requirements**

| Component | Minimum | Recommended |
| :---- | :---- | :---- |
| RAM | 8 GB | 16 GB |
| Storage | 2 GB free | 10 GB free |
| CPU | 4 cores | 8 cores |
| Python | 3.10 | 3.11+ |
| OS | Windows 10, macOS 12, Linux | Windows 11, macOS 14, Linux |

## **6\. INSTALLATION GUIDE**

## **6.1 Prerequisites**

| Requirement | Check Command | Download |
| :---- | :---- | :---- |
| Python 3.9+ | `python --version` | [python.org](https://python.org/) |
| Git | `git --version` | [git-scm.com](https://git-scm.com/) |
| Ollama | `ollama --version` | [ollama.com](https://ollama.com/) |

### **6.2 Windows Installation**

Step 1: Clone the Repository

git clone [https://github.com/VyshnaviER/educational-content-assistant.git](https://github.com/VyshnaviER/educational-content-assistant.git)

cd educational-content-assistant

Step 2: Set Up Python Virtual Environment  
python \-m venv .venv  
.venv\\Scripts\\activate

Step 3: Install Dependencies  
pip install \-r requirements.txt

Step 4: Install Ollama

1. Download the installer from [ollama.com/download](https://ollama.com/download)  
2. Run the executable file  
3. Follow the installation wizard  
4. Verify: `ollama --version`

Step 5: Start Ollama Service  
 Open a NEW terminal window and run:  
ollama serve

Keep this terminal window open while using the application.

Step 6: Download the AI Model  
Open ANOTHER new terminal window and run:  
ollama pull gemma:2b

Step 7: Launch the Application  
streamlit run src/streamlit\_app.py

Step 8: Access the Dashboard  
Open your browser to: [http://localhost:8501](http://localhost:8501/)

### **6.3 macOS Installation**

 1\. Clone the repository  
git clone https://github.com/VyshnaviER/educational-content-assistant.git  
cd educational-content-assistant

 2\. Create and activate virtual environment  
python3 \-m venv .venv  
source .venv/bin/activate

 3\. Install dependencies  
pip install \-r requirements.txt

 4\. Install Ollama  
curl \-fsSL https://ollama.com/install.sh | sh

 5\. Start Ollama service (new terminal, keep open)  
ollama serve

6\. Download AI model (another terminal)  
ollama pull gemma:2b

7\. Launch application  
streamlit run src/streamlit\_app.py

### **6.4 Linux Installation**

 1\. Clone the repository  
git clone https://github.com/VyshnaviER/educational-content-assistant.git  
cd educational-content-assistant

 2\. Create and activate virtual environment  
python3 \-m venv .venv  
source .venv/bin/activate

 3\. Install dependencies  
pip install \-r requirements.txt

 4\. Install Ollama  
curl \-fsSL https://ollama.com/install.sh | sh

 5\. Start Ollama service in background  
ollama serve &

 6\. Download AI model  
ollama pull gemma:2b

 7\. Launch application  
streamlit run src/streamlit\_app.py

**6.5 Docker Installation (Optional)**

Clone the repository  
git clone https://github.com/VyshnaviER/educational-content-assistant.git  
cd educational-content-assistant

Start services using Docker Compose  
docker-compose up \-d

Access the application  
open [http://localhost:8501](http://localhost:8501)

### **6.6 Post-Installation Verification**

 1\. Check Ollama service status  
 curl http://localhost:11434/api/tags

 Expected output:  
 {"models":\[{"name":"gemma:2b", ...}\]}

 2\. Verify model is downloaded  
 ollama list

 Should show: gemma:2b

 3\. Test the application  
 streamlit run src/streamlit\_app.py

 Expected: Browser opens to http://localhost:8501  
 AI Status in sidebar:  Running

### **6.7 Alternative AI Models**

| Model | RAM | Command | Use Case |
| :---- | :---- | :---- | :---- |
| qwen2.5:0.5b | 2 GB | `ollama pull qwen2.5:0.5b` | Fast, lightweight |
| gemma:2b | 4 GB | `ollama pull gemma:2b` | Default, balanced |
| llama2:7b | 8 GB | `ollama pull llama2:7b` | Powerful, detailed |
| mistral:7b | 8 GB | `ollama pull mistral:7b` | Advanced reasoning |

## **7\. USER GUIDE**

## **7.1 Application Interface Overview**

![][image9]

### **7.2 AI Tutor \- User Guide**

Step-by-Step Instructions:

1. Navigate to the AI Tutor tab in the sidebar  
2. Configure Settings:  
   * AI Model: Select from available Ollama models  
   * Answer Style: Simple, Detailed, Technical, With Examples  
   * Difficulty Level: Beginner, Intermediate, Advanced  
3. Enter Your Question in the text area  
4. Click the "Get AI Answer" button  
5. View the AI-generated response  
6. Use Follow-up Options:  
   * "Simplify More" – Get an even simpler explanation  
   * "Related Questions" – Generate follow-up topics

Example Questions by Subject:

| Subject | Example Questions |
| :---- | :---- |
| Biology | "Explain photosynthesis in simple terms" "What is the difference between DNA and RNA?" "How do vaccines work?" |
| Computer Science | "What is object-oriented programming?" "Explain recursion with an example" "How do hash tables work?" |
| Physics | "Explain Newton's three laws of motion" "What is quantum entanglement?" "Why is the sky blue?" |

### **7.3 PDF Summarizer \- User Guide**

Step-by-Step Instructions:

1. Navigate to the PDF Summarizer Pro tab  
2. Upload a PDF or text file (max 10MB, 50 pages)  
3. Configure Summary Settings:  
   * Summary Format: Key Points, Detailed Summary, Chapter-wise, Study Guide  
   * Detail Level: 1 (brief) to 10 (comprehensive)  
   * Focus Areas: Concepts, Examples, Formulas, Key Takeaways  
4. Click "Process & Summarize"  
5. View the generated summary  
6. Optional: Generate study materials  
   * Click "Generate Study Questions" for practice problems  
   * Click "Create Flashcards" for study cards

| Document Type | Format | Detail Level |
| :---- | :---- | :---- |
| Research Paper | Key Points | 5-7 |
| Textbook Chapter | Chapter-wise | 6-8 |
| Lecture Notes | Detailed Summary | 4-6 |
| Study Guide | Study Guide | 7-9 |

### **7.4 Quiz Generator \- User Guide**

Step-by-Step Instructions:

1. Navigate to the Quiz Generator tab  
2. Configure Quiz Parameters:  
   * Topic: Be specific (e.g., "Python functions", not just "Python")  
   * Question Type: Multiple Choice, True/False, Short Answer, Mixed  
   * Number of Questions: 1-20  
   * Difficulty: Easy, Medium, Hard, Expert  
3. Click "Generate Quiz"  
4. Answer the questions  
5. Click "Submit Quiz" to see your score  
6. Review results and explanations

**Scoring Interpretation:**

| Score | Grade | Recommendation |
| :---- | :---- | :---- |
| 100% | A+ | Perfect\! Move to next topic |
| 80-99% | A/B | Good job\! Minor review needed |
| 60-79% | C/D | Fair \- review the material |
| Below 60% | F | Needs work \- try again after studying |

### **7.5 Course Search \- User Guide**

Step-by-Step Instructions:

1. Navigate to the Smart Course Search tab  
2. Select Parameters:  
   * Course: Biology, Computer Science, or Physics  
   * Difficulty Level: Beginner, Intermediate, Advanced  
3. Enter your search term  
4. Click "Search" (or "Browse All Content" to see everything)  
5. Explore Results:  
   * Click  Expand to view full content  
   * Click  Explain this for AI-powered explanation  
6. Learn with simplified definitions and examples

**Content Structure by Level:**

| Level | Content Length | Example |
| :---- | :---- | :---- |
| Beginner | 1-2 sentences | "Cells are the basic unit of life." |
| Intermediate | 3-5 sentences | "Mitochondria produce ATP through cellular respiration..." |
| Advanced | Full paragraph | "The Krebs cycle is a series of chemical reactions..." |

## **8\. DEMO WALKTHROUGH**

### **8.1 Video Demonstration**

Link to video: [https://youtu.be/QLTnXXEg52w](https://youtu.be/QLTnXXEg52w) 

### **8.2 Quick Demo Script** 

| Time | Action | Expected Result |
| :---- | :---- | :---- |
| 0:00 | Launch app: `streamlit run src/streamlit_app.py` | Browser opens to dashboard |
| 0:15 | AI Tutor: Ask "Explain photosynthesis" | 3-5 second response |
| 0:45 | PDF Summarizer: Upload sample PDF | Key points generated |
| 1:15 | Quiz Generator: Topic "Python functions" | 5 questions appear |
| 1:45 | Course Search: Search "neural networks" | Relevant CS content |

### **8.3 Demo Environment Specifications**

| Component | Specification |
| :---- | :---- |
| Device | Laptop \- Dell XPS 15 |
| RAM | 16 GB DDR4 |
| CPU | Intel i7-11800H |
| OS | Windows 11 |
| Model | gemma:2b (default) |
| Response Time | 3-6 seconds average |

*experience may vary based on hardware specifications.*

## 

## ***9\. TROUBLESHOOTING***

### ***9.1 Quick Reference Matrix***

| *Issue* | *Most Likely Cause* | *Solution* | *Time* |
| :---- | :---- | :---- | :---- |
| *AI Tutor: Not Running* | *Ollama service stopped* | *`ollama serve` (new terminal)* | *30s* |
| *Model Not Found* | *Model not downloaded* | *`ollama pull gemma:2b`* | *2-5m* |
| *Slow Responses* | *Insufficient RAM* | *Use `qwen2.5:0.5b` model* | *2m* |
| *Port 8501 in Use* | *Another app on port* | *`--server.port 8502`* | *30s* |
| *PDF Upload Fails* | *Missing PyPDF2* | *`pip install PyPDF2`* | *1m* |
| *Import Errors* | *Missing dependencies* | *`pip install -r requirements.txt`* | *2m* |
| *App Crashes* | *Out of memory* | *Use smaller model, close apps* | *5m* |
| *Connection Refused* | *Ollama not started* | *Run `ollama serve`* | *30s* |

### ***9.2 Detailed Solutions***

***Issue:** AI Tutor Shows "Not Running"*

***Diagnostic:***

*`Check if Ollama is installed`*  
*`ollama --version`*  
*`Check if Ollama service is running`*  
*`curl http://localhost:11434/api/tags`*  
***Solution:***  
*`Start Ollama service in a NEW terminal`*  
*`ollama serve`*

***Issue:** Model Not Found*

***Solution:***

*`Check available models`*  
*`ollama list`*

*`Download the default model`*  
*`ollama pull gemma:2b`*

*`Or try a lightweight alternative`*  
*`ollama pull qwen2.5:0.5b`*

***Issue:** Slow Performance*

***Solution:***

*Switch to lightweight model*

*ollama pull qwen2.5:0.5b*

*Limit parallel requests*

*export OLLAMA\_NUM\_PARALLEL=1*

*Reduce keep-alive time*

*export OLLAMA\_KEEP\_ALIVE=2m*

***Issue:** Port 8501 Already in Use*

***Solution 1:** Use a different port*

*streamlit run src/streamlit\_app.py \--server.port 8502*

*Access at: [http://localhost:8502](http://localhost:8502/)*

## ***10\. FREQUENTLY ASKED QUESTIONS***

*Q: Is it really free?*  
*A: Yes. No subscriptions, no API keys, no credit cards.*

*Q: What are the system requirements?*  
*A: Minimum 8GB RAM, 2GB storage. Recommended 16GB RAM.*

*Q: Why do I need three terminals?*  
*A: Terminal 1: Ollama service (keep open). Terminal 2: Download models. Terminal 3: Run the app.*

*Q: Can I add my own course materials?*  
*A: Yes. Add PDF/text files to `data/sample_courses/` folder.*

*Q: Which AI models can I use?*  
*A: qwen2.5:0.5b (2GB, fast), gemma:2b (4GB, default), llama2:7b (8GB, powerful).*

*Q: Does it work offline?*  
*A: Yes, after downloading the model once.*

*Q: How do I update?*  
*A: `git pull origin main` and `pip install -r requirements.txt --upgrade`*

## ***11\. DEVELOPMENT & CONTRIBUTING***

***Setup:***

*git clone https://github.com/VyshnaviER/educational-content-assistant.git*

*cd educational-content-assistant*

*python \-m venv .venv*

*source .venv/bin/activate  \# Windows: .venv\\Scripts\\activate*

*pip install \-r requirements.txt*

***Areas for Contribution:***

* *New courses (Chemistry, History, Math)*  
* *UI improvements (dark mode, mobile)*  
* *Performance optimization*  
* *Bug fixes*  
* *Documentation*

***Pull Request Process:***

1. *Fork repository*  
2. *Create feature branch*  
3. *Commit changes*  
4. *Open pull request*

## ***12\. REFERENCES & ACKNOWLEDGMENTS***

***Open Source Libraries:***

* *Streamlit \- Web framework*  
* *Ollama \- Local LLM runtime*  
* *LangChain \- RAG pipeline*  
* *ChromaDB \- Vector search*  
* *PyPDF2 \- PDF processing*  
* *Sentence-Transformers \- Embeddings*

***AI Models:***

* *Gemma (Google)*  
* *Qwen (Alibaba)*  
* *Llama (Meta)*  
* *Mistral (Mistral AI)*

## ***14\. CONCLUSION***

*Educational Content Assistant transforms traditional textbooks into an interactive, AI-powered learning experience—all running locally on your device, with no internet required and zero ongoing costs.*

# ***EDUCATIONAL CONTENT ASSISTANT***

*Version 2.0 | February 2026*

*Empowering education through accessible, private AI.*

***Documentation prepared by:** Vyshnavi E R*

***GitHub:** [https://github.com/VyshnaviER/educational-content-assistant](https://github.com/VyshnaviER/educational-content-assistant)*

***Live Demo:** [https://youtu.be/QLTnXXEg52w](https://youtu.be/QLTnXXEg52w)* 

*© 2026 VyshnaviER. MIT License.*

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,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>

[image5]: <data:image/png;base64,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>

[image6]: <data:image/png;base64,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>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgAAAAC0CAYAAADivJSwAAAJXElEQVR4Xu3dv07bWhzA8b5BxdBnqJQJqaISLJU6dunUpSMDPA5IvApIvApC4j1u7+AbGzs5PnZoiJ1cO7/P8JHIwXECy/n6T3I+/PPn3wIAiOVDPgAAHD8BAAABCQAACEgAAEBAAgAAAhIAABDQdAPg/rr4ePKp9rP4sfo59d7x78WiM7b05Xdxmo8dYvzzoju2dPrra2dszPHFt+Tx+V3xnP/vATh6kw6As5uX7jgjeiwuBQBASAIgNAEAEJUACE0AAEQlAEITAABRCYDQBABAVAIgNAEAENV0AwAA2BsBAAABCQAACEgAAEBAAgAAAhIAABDQdAPAxwAPwMcAAaISAAe1nHDLFfiuHnt+938QAABRHUEA1JPqynXx0NlmOw9X0ZbJFQAAUR1JAOw+6Teeby42H5k/3RVnPWGQBsPqvZbbLre5Xf2ueW/rUEn/roeri+L25nq1n8v75nXzsFlu99Tz3gYRAABRCYDGfTkJ9+2n3H/P5FtuvwqGZJs6FpqJvIyE9aT+GhrtAEiiItln+rz8OeMRAABRHUkAJEfKm47it7E60k8m/NZEv9Y3sVeP6zMAmybVfDJv7Sd5rgAAYJ+OIABSL8XteXti3k1yRP8/BUB1SaKJmjf2N4wAAIjqyAIgP13/GgTvn0DL5zX7yff5qn3PQHYJ4I3X2y4AytfvuxwxNgEAENURBED7EkD76H/7AGgdcZ+0b9R7vT+gezSe3gTYncSz1yjH00sVdTD0B0D3/WzzN7yfAACI6ggC4BjlNzbmj8ciAACiEgAT1fpOgvyMxGgEAEBUAiA0AQAQ1XQDAADYGwEAAAEJAAAISAAAQEACAAACEgAAEJAAAICAphsAvgfgAHwPAEBUAmAv6vUJelYRnBYBABCVAGjki/WEmBgFAEBUAqCxaRW/6n3crVccTI7q+7+vf706Yb6iYP9+6hULq/HussP7JQAAohIAjTcCYD0xJ6vylePNJN7z3HI53zwA+vZTbte3HHDn/e2FAACISgA0Nl0CSCf66mi9nsR3CYDOftKj/+x1D0IAAEQlABo9k3ild+Kut19N3N1T99sHQPe5hyMAAKISAI13BkDr1H2P7QLg9T6Cg/6dLQIAICoB0HjvJYB8++YswKbxTftJbhps3xx4CAIAICoBsKPyyD09A5A/ngcBABCVANhVdVd/zxmDWREAAFEJgNAEAEBU0w0AAGBvBAAABCQAACAgAQAAAQkAAAhIAABAQNMNAB8DPAAfAwSISgCEJgAAohIAoQkAgKgEQGgCACAqARCaAACIatIBsF5s52fxo7XE7q7j34tFZ2zpy+/iNB87xPjnRXds6fTX187Y6/hZZ+zt7fvHF9+SxwIAIKTpBsBMPN9czHAZYACiEwADCQAA5kgADCQAAJgjATCQAABgjgTAQAIAgDkSAAMJAADmSAAAQEACAAACEgAAEJAAAICABAAABCQAACAgATCQjwECMEcCYCABAMAcCYCBBAAAcyQABhIAAMyRABhIAAAwRwJgIAEAwBwJgIEEAABzJAAGEgAAzJEAGEgAADBHAmAgAQDAHAmAgQQAAHMkAAYSAADMkQAAgIAEAAAEJAAAICABAAABCQAACEgAAEBAAgAAAhIAABCQAACAgAQAAAQkAHbyWFyefCo+5q4ee7YFgOkRALu6v84C4KK4ferZDgAmSADs7KW4PXf0D8A8CYAhVmcBHP0DMC8CYJD6LICjfwBmRgAMdX/n6B+A2REAABCQAACAgAQAAAQkAAAgIAEAAAEJAAAISAAAQEACAAACEgAAEJAAAICABAAABCQAACAgAQAAAQkAAAhougFwf118PPlU+1n8WP2ceu/492LRGVv68rs4zccOMf550R1bOv31tTM25vjiW/L4/K54zv/3ABy9SQfA2c1Ld5wRPRaXAgAgJAEQmgAAiEoAhCYAAKISAKEJAICoBEBoAgAgKgEQmgAAiGq6AQAA7I0AAICABAAABCQAACAgAQAAAQkAAAhougHgY4AH4GOAAFEJgINZTrb1Cnz53/Vw9am4vM+3PwQBABDVkQTAS3F73ixxe108dH6/hae74ixZMnf7136f55uLzr4FAACHdgQB8Dr5D55AywC4elz/nIREOWn3hUE6/rF57vJ9r36u3ttFcfu0fp1WAGTRUVlNyGnUjPD39RIAAFHNPwDSiXuIPACaibG1/2RCT7dJvScAan1nAPq2G58AAIhq/gFQTbh3I18C6D/6f9VM6M0RevZ6IwXA6v2METcbCQCAqI4jAFaTcv8Eu5XVkX570v77/uqb+5qJdKwAaFR/377uSRAAAFHNPwCySwDtybQ+St9mkkv3k07i5c9/fX4ZAfWZgOTSwOvZg78HQN9YSysqxiQAAKKafwD82XAzXmXHAMhuLCyjYn0JIJnok0sDneio3kt5aSK5Z6D3UkL2u1Y8ZK85OgEAENVRBAC7EgAAUQmA0AQAQFQCIDQBABDVdAMAANgbAQAAAQkAAAhIAABAQAIAAAISAAAQkAAAgICmGwC+B+AAfA8AQFQCYCv1in+DFuSp93Gyr5X9diEAAKISALX2gj9vLM870F9X/jsoAQAQlQCotZYRrlbna1br23zk3rsKYfW+7958TmusXOp3FR7pa6bLCCfLDY9KAABEJQBqrQCoH6ev35m4y0jomzyrCX3TRN6zn/y5dUi0ttvb/0IAAEQlAGp5AOQTdf74nz8vxe15edSeHZknk/g2+03PMLTOJJSBUf/8cNWOiPEIAICoBEAtn6jzx92Ju1FP4M1E2gmAt88AtM40tJ5bBkYZF8v9D7r58C0CACAqAVBrTfjVafz2kX0+cbcl1+jTSby6l+Dt/aSvW92ImEz25baXV9d7uyFRAADEJQBq7U8BJJN2NYmnv6uP6LPxdjzkN/V1t1/9Ltn+8mZ92n/9nH3c/NcQAABRCYCxZZcABtn7/0AAAEQlAMY2RgA0Zwv2PjkLAICoBEBoAgAgqukGAACwNwIAAAISAAAQkAAAgIAEAAAEJAAAIKDpBoCPAR6AjwECRCUAQhMAAFEJgNAEAEBUAiA0AQAQlQAITQAARDXpAFgvnfuz+NFaSnfX8e/FojO29OV3cZqPHWL886I7tnT662tnbMzxxbfksQAACGm6AQAA7I0AAICABAAABCQAACAgAQAAAQkAAAhIAABAQP8B5qPo1aJfyMQAAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,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>

[image9]: <data:image/png;base64,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>