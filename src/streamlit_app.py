import streamlit as st
import sys
import os
import tempfile
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

st.set_page_config(page_title="Educational Assistant", layout="wide")
st.title("🎓 Educational Assistant Pro")

try:
    from educational_assistant import KnowledgeBase
    kb = KnowledgeBase()
    kb.load_courses()
    COURSES_LOADED = True
except Exception as e:
    st.error(f"Course Error: {e}")
    kb = None
    COURSES_LOADED = False

# Check Ollama status
try:
    import ollama
    OLLAMA_AVAILABLE = True
    try:
        ollama.list()
        OLLAMA_RUNNING = True
    except:
        OLLAMA_RUNNING = False
except ImportError:
    OLLAMA_AVAILABLE = False
    OLLAMA_RUNNING = False

# Sidebar status
st.sidebar.header("🔧 Status")
if COURSES_LOADED:
    st.sidebar.success(f"📚 {len(kb.data)} course items")
if OLLAMA_RUNNING:
    st.sidebar.success("🤖 AI: Available")
elif OLLAMA_AVAILABLE:
    st.sidebar.warning("🤖 AI: Install ollama package")
else:
    st.sidebar.error("🤖 AI: Not running")

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Course Search", 
    "🤖 AI Tutor", 
    "📄 PDF Summarizer", 
    "❓ Quiz Generator"
])

# TAB 1: Course Search
with tab1:
    st.subheader("🔍 Search Course Materials")
    
    if not COURSES_LOADED:
        st.warning("Course materials not loaded")
    else:
        question = st.text_input("Search in your courses:", key="search_q")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("🔎 Search Courses", use_container_width=True) and question:
                with st.spinner("Searching..."):
                    results = kb.search(question, max_results=5)
                    if results:
                        st.subheader(f"📚 Found {len(results)} matches:")
                        for i, r in enumerate(results, 1):
                            with st.expander(f"Match {i} (Relevance: {r['score']}/5)"):
                                st.write(r['content'])
                                st.caption(f"Source: {r['source']}")
                    else:
                        st.warning("No matches found.")
        
        with col2:
            if st.button("📋 Show All Courses", use_container_width=True):
                st.subheader("📚 All Available Courses:")
                if kb.data:
                    sources = set(r['source'] for r in kb.data)
                    for source in sources:
                        st.write(f"• {source}")

# TAB 2: AI Tutor
with tab2:
    st.subheader("🤖 AI Tutor")
    
    if not OLLAMA_RUNNING:
        st.warning("Ollama AI not available. Install and run Ollama first.")
        st.info("""
        **To enable AI:**
        1. Download Ollama from https://ollama.com/
        2. Run: `ollama serve` (in terminal)
        3. Pull model: `ollama pull gemma:2b`
        """)
    else:
        question = st.text_area("Ask any educational question:", 
                               height=120,
                               placeholder="e.g., Explain quantum physics in simple terms...")
        
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            model = st.selectbox("AI Model:", ["gemma:2b", "qwen3:4b", "qwen3:8b"], index=0)
        
        with col2:
            style = st.selectbox("Answer Style:", ["Simple", "Detailed", "Step-by-step"])
        
        with col3:
            complexity = st.selectbox("Level:", ["Beginner", "Intermediate", "Advanced"])
        
        if st.button("🎯 Get AI Answer", type="primary") and question:
            with st.spinner(f"🤖 {model} is thinking..."):
                try:
                    prompt = f"""You are an educational tutor. Answer this question for a {complexity.lower()} level student in a {style.lower()} style:

QUESTION: {question}

ANSWER:"""
                    
                    response = ollama.generate(
                        model=model,
                        prompt=prompt,
                        options={'num_predict': 300}
                    )
                    
                    st.subheader("🧠 AI Answer:")
                    st.markdown(response['response'])
                    
                    # Additional options
                    with st.expander("💡 Ask follow-up"):
                        follow_up = st.text_input("Follow-up question:")
                        if st.button("Ask Follow-up"):
                            with st.spinner("Thinking..."):
                                follow_response = ollama.generate(
                                    model=model,
                                    prompt=f"Previous context: {response['response']}\n\nFollow-up: {follow_up}\nAnswer:"
                                )
                                st.write(follow_response['response'])
                    
                    st.success("✅ Answered!")
                    
                except Exception as e:
                    st.error(f"AI error: {str(e)[:100]}")

# TAB 3: PDF Summarizer
with tab3:
    st.subheader("📄 PDF Summarizer")
    st.write("Upload a PDF and get a summary (basic text extraction)")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        st.success(f"📄 Uploaded: {uploaded_file.name}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            summary_length = st.select_slider(
                "Summary Length:",
                options=["Very Short", "Short", "Medium", "Detailed"]
            )
        
        with col2:
            focus = st.multiselect(
                "Focus on:",
                ["Key Points", "Examples", "Definitions", "Conclusions"],
                default=["Key Points"]
            )
        
        if st.button("📋 Generate Summary"):
            with st.spinner("Processing PDF..."):
                try:
                    # Basic PDF text extraction (simplified)
                    import PyPDF2
                    
                    pdf_text = ""
                    with open(tmp_path, 'rb') as file:
                        pdf_reader = PyPDF2.PdfReader(file)
                        for page in pdf_reader.pages[:5]:  # First 5 pages only
                            text = page.extract_text()
                            if text:
                                pdf_text += text + "\n\n"
                    
                    if pdf_text:
                        # Show extracted text
                        with st.expander("📖 Extracted Text (first 1000 chars)"):
                            st.text(pdf_text[:1000] + "...")
                        
                        # Generate summary with AI if available
                        if OLLAMA_RUNNING:
                            st.subheader("🤖 AI Summary:")
                            
                            prompt = f"""Summarize this text for educational purposes.
                            Length: {summary_length}
                            Focus on: {', '.join(focus)}
                            
                            TEXT:
                            {pdf_text[:2000]}...
                            
                            SUMMARY:"""
                            
                            try:
                                response = ollama.generate(
                                    model="gemma:2b",
                                    prompt=prompt,
                                    options={'num_predict': 200}
                                )
                                st.markdown(response['response'])
                                st.success("✅ Summary generated!")
                            except:
                                st.info("AI summary failed. Showing extracted text.")
                                st.write(pdf_text[:500])
                        else:
                            st.subheader("📝 Extracted Content:")
                            st.write(pdf_text[:1000])
                            st.info("Enable AI for better summaries")
                    
                    # Clean up
                    os.unlink(tmp_path)
                    
                except ImportError:
                    st.error("Install: pip install PyPDF2")
                except Exception as e:
                    st.error(f"Error: {e}")

# TAB 4: Quiz Generator
with tab4:
    st.subheader("❓ Quiz Generator")
    
    topic = st.text_input("Enter a topic for quiz:", 
                         placeholder="e.g., Photosynthesis, Python Programming, World History")
    
    col1, col2 = st.columns(2)
    with col1:
        num_questions = st.slider("Number of questions:", 1, 10, 5)
    
    with col2:
        difficulty = st.select_slider("Difficulty:", 
                                     options=["Easy", "Medium", "Hard"])
    
    question_types = st.multiselect(
        "Question types:",
        ["Multiple Choice", "True/False", "Short Answer", "Fill in Blank"],
        default=["Multiple Choice"]
    )
    
    if st.button("🎯 Generate Quiz") and topic:
        if OLLAMA_RUNNING:
            with st.spinner("Creating quiz..."):
                try:
                    prompt = f"""Create a {difficulty.lower()} quiz about {topic} with {num_questions} questions.
                    Question types: {', '.join(question_types)}.
                    
                    Format each question as:
                    Q1. [Question text]
                    A) [Option A]
                    B) [Option B]
                    C) [Option C]
                    D) [Option D]
                    Answer: [Correct letter]
                    
                    Explanation: [Brief explanation]
                    
                    QUIZ:"""
                    
                    response = ollama.generate(
                        model="gemma:2b",
                        prompt=prompt,
                        options={'num_predict': 500}
                    )
                    
                    st.subheader(f"📝 Quiz: {topic}")
                    st.markdown(response['response'])
                    
                    # Quiz interaction
                    st.markdown("---")
                    st.subheader("📊 Take the Quiz")
                    
                    quiz_text = response['response']
                    questions = quiz_text.split('\n\n')
                    
                    user_answers = {}
                    for i, q in enumerate(questions[:num_questions]):
                        if '?' in q:
                            st.write(f"**Q{i+1}.**")
                            lines = q.split('\n')
                            question_text = lines[0]
                            st.write(question_text)
                            
                            options = [line for line in lines[1:] if line.strip() and ')' in line]
                            for opt in options:
                                st.write(opt)
                            
                            user_answer = st.text_input(f"Your answer for Q{i+1} (A/B/C/D):", 
                                                       key=f"q{i}")
                            user_answers[i] = user_answer
                    
                    if st.button("Check Answers"):
                        st.success("Quiz submitted! (Grading feature would be added)")
                        
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("AI required for quiz generation. Enable Ollama in AI Tutor tab.")

# Footer
st.markdown("---")
cols = st.columns(3)
with cols[0]:
    st.caption("🔍 Course Search")
with cols[1]:
    st.caption("🤖 AI Tutor")
with cols[2]:
    st.caption(f"💻 Local Processing")
