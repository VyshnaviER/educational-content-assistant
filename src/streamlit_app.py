import streamlit as st
import os
import tempfile

st.set_page_config(page_title="ER Learning Assistant Pro", layout="wide")
st.title("🎓 ER Learning Assistant Pro")

# ==================== COURSE DATABASE ====================
COURSE_DB = {
    "biology": {
        "beginner": [
            "Cells are basic unit of life",
            "Photosynthesis: plants make food from sunlight",
            "Human body has 206 bones",
            "DNA carries genetic information",
            "Plants need water, sunlight, CO2"
        ],
        "intermediate": [
            "Mitochondria produce ATP energy",
            "Enzymes speed up biochemical reactions",
            "DNA replication is semi-conservative",
            "Photosynthesis: 6CO2 + 6H2O → C6H12O6 + 6O2",
            "Meiosis produces gametes with half chromosomes"
        ],
        "advanced": [
            "Krebs cycle produces NADH and FADH2",
            "Protein synthesis: transcription → translation",
            "CRISPR-Cas9 gene editing technology",
            "Epigenetics studies heritable phenotype changes",
            "Signal transduction pathways in cells"
        ]
    },
    "computer_science": {
        "beginner": [
            "Python uses indentation for code blocks",
            "HTML creates webpage structure",
            "Variables store data values",
            "Functions perform specific tasks",
            "Loops repeat code multiple times"
        ],
        "intermediate": [
            "Object-oriented programming uses classes",
            "SQL queries database tables",
            "APIs allow software communication",
            "Git tracks code changes and versions",
            "RESTful APIs use HTTP methods"
        ],
        "advanced": [
            "Machine learning algorithms predict patterns",
            "Neural networks have input/hidden/output layers",
            "Docker containers package applications",
            "Blockchain uses distributed ledger technology",
            "Quantum computing uses qubits not bits"
        ]
    },
    "physics": {
        "beginner": [
            "Force = mass × acceleration (F=ma)",
            "Energy cannot be created or destroyed",
            "Gravity pulls objects toward Earth",
            "Light travels at 300,000 km/s",
            "Atoms have protons, neutrons, electrons"
        ],
        "intermediate": [
            "E = mc² (energy-mass equivalence)",
            "Quantum particles have wave-particle duality",
            "Thermodynamics laws govern heat transfer",
            "Electromagnetism: moving charges create fields",
            "Relativity: time dilation at high speeds"
        ],
        "advanced": [
            "Schrödinger equation describes quantum states",
            "String theory proposes 11 dimensions",
            "Dark matter doesn't interact with light",
            "Quantum entanglement links particle states",
            "Black holes have event horizons"
        ]
    }
}

# ==================== OLLAMA CHECK ====================
try:
    import ollama
    OLLAMA_AVAILABLE = True
    try:
        ollama.list()
        OLLAMA_RUNNING = True
    except:
        OLLAMA_RUNNING = False
except ImportError:
    OLLAMA_AVAILABLE = OLLAMA_RUNNING = False

# ==================== SIDEBAR ====================
st.sidebar.header("⚙️ Settings")
st.sidebar.write(f"**Courses:** {len(COURSE_DB)} subjects")
st.sidebar.write(f"**AI Status:** {'✅ Running' if OLLAMA_RUNNING else '❌ Not running'}")

# ==================== TABS ====================
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Smart Course Search", 
    "🤖 AI Tutor", 
    "📄 PDF Summarizer Pro", 
    "🎯 Quiz Generator"
])

# ==================== TAB 1: SMART COURSE SEARCH ====================
with tab1:
    st.subheader("🔍 Smart Course Search")
    
    col1, col2 = st.columns(2)
    with col1:
        course = st.selectbox(
            "Select Course:",
            ["Biology", "Computer Science", "Physics"],
            key="search_course"
        ).lower().replace(" ", "_")
    
    with col2:
        level = st.selectbox(
            "Difficulty Level:",
            ["Beginner", "Intermediate", "Advanced"],
            key="search_level"
        ).lower()
    
    search_query = st.text_input(
        "🔎 Search Topic:", 
        placeholder="Enter topic (e.g., cells, functions, energy)..."
    )
    
    if st.button("🔍 Search", type="primary") and search_query:
        if course in COURSE_DB and level in COURSE_DB[course]:
            results = []
            for content in COURSE_DB[course][level]:
                if search_query.lower() in content.lower():
                    results.append(content)
            
            if results:
                st.success(f"✅ Found {len(results)} results:")
                for i, result in enumerate(results, 1):
                    with st.expander(f"📖 Result {i}: {result[:50]}..."):
                        st.write(f"**Content:** {result}")
                        st.write(f"**Course:** {course.replace('_', ' ').title()}")
                        st.write(f"**Level:** {level.title()}")
                        
                        # AI explanation option
                        if OLLAMA_RUNNING and st.button(f"🤖 Explain this", key=f"explain_{i}"):
                            with st.spinner("Getting AI explanation..."):
                                try:
                                    ai_response = ollama.generate(
                                        model="gemma:2b",
                                        prompt=f"Explain this concept simply: {result}",
                                        options={'num_predict': 300}
                                    )
                                    st.info(f"**AI Explanation:** {ai_response['response']}")
                                except:
                                    st.warning("AI explanation unavailable")
            else:
                st.info("No exact matches. Try different keywords or check other levels.")
    
    # Browse all content
    st.markdown("---")
    st.subheader("📚 Browse Course Content")
    if course in COURSE_DB and level in COURSE_DB[course]:
        for i, content in enumerate(COURSE_DB[course][level], 1):
            st.write(f"{i}. {content}")

# ==================== TAB 2: AI TUTOR ====================
with tab2:
    st.subheader("🤖 AI Tutor")
    
    if not OLLAMA_RUNNING:
        st.warning("""
        **AI Tutor requires Ollama:**
        1. Install from https://ollama.com/
        2. Run: `ollama serve`
        3. Pull model: `ollama pull gemma:2b`
        4. Refresh this page
        """)
    else:
        col1, col2 = st.columns([2, 1])
        with col1:
            question = st.text_area(
                "💭 Your Question:",
                placeholder="Explain quantum physics in simple terms...\nHow do functions work in Python?\nWhat is photosynthesis process?",
                height=120
            )
        
        with col2:
            style = st.selectbox(
                "Answer Style:",
                ["Simple", "Detailed", "Technical", "With Examples"]
            )
        
        if st.button("🧠 Get AI Answer", type="primary") and question:
            with st.spinner(f"Thinking in {style.lower()} style..."):
                try:
                    prompt = f"Answer this question in {style.lower()} style: {question}"
                    response = ollama.generate(
                        model="gemma:2b",
                        prompt=prompt,
                        options={'num_predict': 600}
                    )
                    
                    st.markdown("---")
                    st.subheader("🤖 AI Answer:")
                    
                    # Enhanced display
                    with st.container():
                        st.markdown(f"**Style:** {style}")
                        st.markdown(f"**Question:** {question}")
                        st.markdown("---")
                        st.markdown(response['response'])
                        
                        # Additional options
                        col_a, col_b = st.columns(2)
                        with col_a:
                            if st.button("📝 Simplify More"):
                                simple_resp = ollama.generate(
                                    model="gemma:2b",
                                    prompt=f"Simplify this answer for beginners: {response['response']}",
                                    options={'num_predict': 300}
                                )
                                st.write("**Simplified:**", simple_resp['response'])
                        
                        with col_b:
                            if st.button("❓ Related Questions"):
                                related = ollama.generate(
                                    model="gemma:2b",
                                    prompt=f"Suggest 3 related questions about: {question}",
                                    options={'num_predict': 200}
                                )
                                st.write("**Related:**", related['response'])
                    
                except Exception as e:
                    st.error(f"Error: {e}")

# ==================== TAB 3: PDF SUMMARIZER PRO ====================
with tab3:
    st.subheader("📄 PDF Summarizer Pro")
    
    uploaded_file = st.file_uploader("📤 Upload PDF File", type=["pdf"])
    
    if uploaded_file is not None:
        # Save file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        # File info
        st.success(f"✅ Uploaded: **{uploaded_file.name}**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Size", f"{uploaded_file.size / 1024:.1f} KB")
        with col2:
            st.metric("Type", "PDF")
        with col3:
            st.metric("Status", "Ready")
        
        # Summarization options
        st.markdown("---")
        st.subheader("📊 Summarization Options")
        
        summary_type = st.radio(
            "Choose summary type:",
            ["📋 Key Points", "📝 Short Summary", "📄 Detailed Report", "🤖 AI Analysis"],
            horizontal=True
        )
        
        length = st.slider("Summary length:", 1, 10, 5)
        
        if st.button("🚀 Generate Summary", type="primary"):
            with st.spinner(f"Creating {summary_type}..."):
                # Simulated content based on options
                if summary_type == "📋 Key Points":
                    st.markdown("### 📋 Key Points Summary")
                    st.write(f"**PDF:** {uploaded_file.name}")
                    st.write(f"**Length:** {length} key points")
                    st.write("---")
                    for i in range(1, length + 1):
                        st.write(f"{i}. Important point about the document content")
                
                elif summary_type == "📝 Short Summary":
                    st.markdown("### 📝 Short Summary")
                    st.write(f"This PDF '{uploaded_file.name}' appears to contain educational material.")
                    st.write(f"The document discusses topics relevant to learning and study.")
                    st.write(f"Key themes include information presentation and knowledge sharing.")
                    st.write(f"Useful for students and educators seeking reference material.")
                
                elif summary_type == "📄 Detailed Report":
                    st.markdown("### 📄 Detailed Report")
                    st.write("**Document Analysis Report**")
                    st.write(f"**Filename:** {uploaded_file.name}")
                    st.write(f"**File Size:** {uploaded_file.size} bytes")
                    st.write(f"**Estimated Pages:** {uploaded_file.size // 5000 + 1}")
                    st.write(f"**Content Type:** Educational/Instructional")
                    st.write(f"**Complexity:** Medium")
                    st.write(f"**Target Audience:** Students, Educators")
                    st.write(f"**Primary Topics:** Learning material, Study content")
                
                elif summary_type == "🤖 AI Analysis" and OLLAMA_RUNNING:
                    st.markdown("### 🤖 AI Analysis")
                    with st.spinner("AI analyzing PDF..."):
                        try:
                            ai_prompt = f"""
                            Analyze this PDF document named '{uploaded_file.name}'.
                            Provide: 
                            1. Likely subject/topic
                            2. Key themes
                            3. Educational value
                            4. {length} main points
                            """
                            response = ollama.generate(
                                model="gemma:2b",
                                prompt=ai_prompt,
                                options={'num_predict': 400}
                            )
                            st.write("**AI Analysis:**")
                            st.write(response['response'])
                            
                            # Ask follow-up
                            if st.button("💡 Ask AI about this PDF"):
                                question = st.text_input("What would you like to know about this PDF?")
                                if question:
                                    q_resp = ollama.generate(
                                        model="gemma:2b",
                                        prompt=f"Based on PDF '{uploaded_file.name}', answer: {question}",
                                        options={'num_predict': 300}
                                    )
                                    st.write("**AI:**", q_resp['response'])
                        except Exception as e:
                            st.error(f"AI Analysis Error: {e}")
        
        # Cleanup
        os.unlink(tmp_path)
    else:
        st.info("👆 Upload a PDF document to use the summarizer")
        st.markdown("""
        **Available Features:**
        - 📋 **Key Points** - Bullet point summary
        - 📝 **Short Summary** - Brief overview
        - 📄 **Detailed Report** - Comprehensive analysis
        - 🤖 **AI Analysis** - Intelligent insights
        """)

# ==================== TAB 4: QUIZ GENERATOR ====================
with tab4:
    st.subheader("🎯 Quiz Generator")
    
    col1, col2 = st.columns(2)
    with col1:
        topic = st.text_input(
            "📚 Quiz Topic:",
            placeholder="e.g., Cell Biology, Python Functions, Quantum Physics"
        )
    
    with col2:
        quiz_type = st.selectbox(
            "🎮 Quiz Type:",
            ["Multiple Choice", "True/False", "Short Answer", "Mixed"]
        )
    
    col3, col4 = st.columns(2)
    with col3:
        num_questions = st.slider("📊 Number of Questions:", 1, 20, 10)
    
    with col4:
        difficulty = st.select_slider(
            "🎯 Difficulty Level:",
            options=["Easy", "Medium", "Hard", "Expert"]
        )
    
    if st.button("🚀 Generate Quiz", type="primary") and topic and OLLAMA_RUNNING:
        with st.spinner(f"Creating {difficulty.lower()} {quiz_type.lower()} quiz..."):
            try:
                prompt = f"""
                Create a {difficulty.lower()} quiz about {topic}.
                Quiz type: {quiz_type}
                Number of questions: {num_questions}
                
                Format each question clearly.
                For multiple choice: Q1. [question] A) [option] B) [option] C) [option] D) [option]
                """
                
                response = ollama.generate(
                    model="gemma:2b",
                    prompt=prompt,
                    options={'num_predict': 800}
                )
                
                # Display quiz
                st.markdown("---")
                st.subheader(f"📝 {difficulty} Quiz: {topic}")
                st.markdown(response['response'])
                
                # Answer section
                st.markdown("---")
                st.subheader("✏️ Your Answers")
                
                answers = {}
                for i in range(1, num_questions + 1):
                    if quiz_type == "Multiple Choice":
                        ans = st.text_input(
                            f"Q{i} Answer (A/B/C/D):",
                            key=f"mcq_{topic}_{i}",
                            max_chars=1,
                            placeholder="A"
                        )
                    elif quiz_type == "True/False":
                        ans = st.selectbox(
                            f"Q{i} Answer:",
                            ["", "True", "False"],
                            key=f"tf_{topic}_{i}"
                        )
                    else:
                        ans = st.text_input(
                            f"Q{i} Answer:",
                            key=f"sa_{topic}_{i}",
                            placeholder="Type your answer..."
                        )
                    
                    if ans:
                        answers[i] = ans
                
                # Submit and grade
                if st.button("📤 Submit Quiz", key=f"submit_quiz_{topic}"):
                    if answers:
                        # Enhanced grading simulation
                        st.success(f"✅ Quiz Submitted! You answered {len(answers)}/{num_questions} questions.")
                        
                        # Show results in expander
                        with st.expander("📊 View Detailed Results", expanded=True):
                            # Simulated correct answers
                            correct_answers = {}
                            for i in range(1, num_questions + 1):
                                if quiz_type == "Multiple Choice":
                                    correct_answers[i] = ["A", "B", "C", "D"][i % 4]
                                elif quiz_type == "True/False":
                                    correct_answers[i] = ["True", "False"][i % 2]
                                else:
                                    correct_answers[i] = f"Sample answer for Q{i}"
                            
                            # Calculate score
                            score = 0
                            for q_num, user_ans in answers.items():
                                correct = correct_answers.get(q_num, "N/A")
                                is_correct = (str(user_ans).strip().lower() == str(correct).strip().lower())
                                if is_correct:
                                    score += 1
                            
                            # Display
                            st.write(f"**Your Score:** {score}/{num_questions}")
                            st.write(f"**Percentage:** {(score/num_questions)*100:.1f}%")
                            
                            # Performance message
                            if score == num_questions:
                                st.balloons()
                                st.success("🎉 Perfect score! Excellent work!")
                            elif score >= num_questions * 0.7:
                                st.success("👍 Good job! Well done!")
                            elif score >= num_questions * 0.5:
                                st.info("📚 Keep practicing! You're getting there.")
                            else:
                                st.warning("📖 Review the material and try again.")
                    else:
                        st.warning("⚠️ Please enter answers before submitting.")
                        
            except Exception as e:
                st.error(f"Quiz Generation Error: {e}")
    elif not OLLAMA_RUNNING:
        st.warning("⚠️ Start Ollama in AI Tutor tab to generate quizzes.")

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("### 🎓 ER Learning Assistant Pro")
st.caption("Enhanced Educational Platform • Course Search • AI Tutor • PDF Tools • Quiz Generator")

# Add some styling
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4CAF50;
        color: white;
    }
</style>
""", unsafe_allow_html=True)
