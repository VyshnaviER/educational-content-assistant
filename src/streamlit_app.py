
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
st.sidebar.write(f"**Courses:** Biology, Computer Science")
st.sidebar.write(f"**AI Status:** {'✅ Running' if OLLAMA_RUNNING else '❌ Not running'}")

# ==================== TABS ====================
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Smart Course Search", 
    "🤖 AI Tutor", 
    "📄 PDF Summarizer Pro", 
    "🎯 Quiz Generator"
])
# ==================== TAB 1: SMART COURSE SEARCH ====================
# ==================== TAB 1: SMART COURSE SEARCH ====================
with tab1:
    st.subheader("🔍 Smart Course Search")
    
    # Use hardcoded course database
    if 'course_data' not in st.session_state:
        st.session_state.course_data = {
            "biology": {
                "beginner": [
                    "Cells are the basic unit of life. All living organisms are composed of cells.",
                    "Photosynthesis is the process where plants make food from sunlight, water and CO2.",
                    "DNA (Deoxyribonucleic acid) carries genetic information in all living organisms.",
                    "The human body has 206 bones that provide structure and protection.",
                    "Plants need water, sunlight, and carbon dioxide to perform photosynthesis."
                ],
                "intermediate": [
                    "Mitochondria are the powerhouses of the cell, producing ATP through cellular respiration.",
                    "Enzymes are biological catalysts that speed up biochemical reactions.",
                    "DNA replication is semi-conservative, each new DNA molecule has one original strand.",
                    "The photosynthesis equation: 6CO2 + 6H2O → C6H12O6 + 6O2",
                    "Meiosis produces gametes with half the chromosome number for sexual reproduction."
                ],
                "advanced": [
                    "The Krebs cycle occurs in mitochondria and produces NADH and FADH2 for electron transport.",
                    "Protein synthesis involves transcription (DNA to mRNA) and translation (mRNA to protein).",
                    "CRISPR-Cas9 is a gene editing technology that allows precise DNA modifications.",
                    "Epigenetics studies heritable phenotype changes without altering DNA sequence.",
                    "Signal transduction pathways convert extracellular signals into cellular responses."
                ]
            },
            "computer_science": {
                "beginner": [
                    "Python uses indentation (whitespace) to define code blocks instead of braces.",
                    "HTML (Hypertext Markup Language) creates the structure of webpages.",
                    "Variables store data values in computer memory for later use.",
                    "Functions are reusable blocks of code that perform specific tasks.",
                    "Loops (for, while) allow code to repeat multiple times efficiently."
                ],
                "intermediate": [
                    "Object-oriented programming (OOP) uses classes and objects to organize code.",
                    "SQL (Structured Query Language) is used to query and manage database tables.",
                    "APIs (Application Programming Interfaces) allow different software applications to communicate.",
                    "Common data structures include lists, dictionaries, stacks, and queues.",
                    "Version control systems like Git track changes in code over time."
                ],
                "advanced": [
                    "Machine learning algorithms learn patterns from data to make predictions.",
                    "Neural networks are computing systems inspired by biological brain structure.",
                    "Cloud computing delivers computing services over the internet on demand.",
                    "Cybersecurity protects computer systems from theft, damage, or disruption.",
                    "Blockchain is a distributed ledger technology that enables secure, transparent transactions."
                ]
            }
        }
    
    # Subject and level selection
    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox("📚 Select Subject:", ["biology", "computer_science"], 
                              format_func=lambda x: x.title())
    with col2:
        level = st.selectbox("🎯 Select Level:", ["beginner", "intermediate", "advanced"],
                            format_func=lambda x: x.title())
    
    # Get topics for selected subject and level
    topics = st.session_state.course_data[subject][level]
    
    # Search box
    search_query = st.text_input("🔍 Search topics:", 
                                placeholder=f"Search in {subject.title()} - {level.title()}...")
    
    # Filter topics based on search
    if search_query:
        filtered_topics = [topic for topic in topics if search_query.lower() in topic.lower()]
    else:
        filtered_topics = topics
    
    # Display results
    st.markdown("---")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if search_query:
            st.subheader(f"📋 Search Results: {len(filtered_topics)} matches")
        else:
            st.subheader(f"📋 All Topics: {len(filtered_topics)} topics")
    with col2:
        st.info(f"📚 {subject.title()} - {level.title()}")
    
    # Show topics with expanders
    if filtered_topics:
        for i, topic in enumerate(filtered_topics, 1):
            with st.expander(f"📖 Topic {i}: {topic[:60]}..."):
                st.markdown(f"**Complete Content:**")
                st.write(topic)
                st.caption(f"📌 Subject: {subject.title()} | Level: {level.title()}")
    else:
        st.warning("⚠️ No matching topics found. Try different keywords.")
        st.info("💡 Suggestions: Try 'cell', 'DNA', 'Python', 'algorithm'")
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
    st.write("Upload a PDF or textbook to get AI-powered analysis and summaries")

    uploaded_file = st.file_uploader("📤 Upload PDF File", type=["pdf", "txt"], 
                                     help="Supports PDF and text files up to 10MB")

    if uploaded_file is not None:
        # Save file
        with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{uploaded_file.name.split(".")[-1]}') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        # File info
        st.success(f"✅ Uploaded: **{uploaded_file.name}**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Size", f"{uploaded_file.size / 1024:.1f} KB")
        with col2:
            file_type = uploaded_file.name.split('.')[-1].upper()
            st.metric("Type", file_type)
        with col3:
            st.metric("Pages", "Processing...")

        st.markdown("---")
        
        # Processing options
        col1, col2 = st.columns(2)
        with col1:
            summary_type = st.selectbox(
                "Summary Format:",
                ["Key Points", "Detailed Summary", "Chapter-wise", "Study Guide"],
                help="Choose how you want the content summarized"
            )
        
        with col2:
            detail_level = st.slider(
                "Detail Level:", 
                1, 10, 5,
                help="1 = Very brief, 10 = Very detailed"
            )

        # Advanced options
        with st.expander("⚙️ Advanced Options"):
            focus_areas = st.multiselect(
                "Focus on specific aspects:",
                ["Concepts & Definitions", "Examples & Applications", 
                 "Formulas & Equations", "Key Takeaways", "Practice Problems"],
                default=["Concepts & Definitions", "Key Takeaways"]
            )
            
            include_examples = st.checkbox("Include examples", value=True)
            target_audience = st.select_slider(
                "Target Audience:",
                options=["Beginner", "Intermediate", "Advanced", "Expert"]
            )

        if st.button("🚀 Process & Summarize", type="primary"):
            with st.spinner(f"Reading {uploaded_file.name}..."):
                try:
                    extracted_text = ""
                    
                    # Handle different file types
                    if uploaded_file.type == "application/pdf" or uploaded_file.name.endswith('.pdf'):
                        # Extract text from PDF
                        try:
                            import PyPDF2
                            with open(tmp_path, 'rb') as file:
                                pdf_reader = PyPDF2.PdfReader(file)
                                num_pages = len(pdf_reader.pages)
                                
                                # Update page count
                                col3.metric("Pages", num_pages)
                                
                                # Extract text from each page
                                for page_num in range(min(num_pages, 50)):  # Limit to 50 pages for performance
                                    page = pdf_reader.pages[page_num]
                                    text = page.extract_text()
                                    if text:
                                        extracted_text += f"\n--- Page {page_num + 1} ---\n{text}\n"
                                
                                if num_pages > 50:
                                    st.warning(f"Processed first 50 of {num_pages} pages for performance.")
                        
                        except ImportError:
                            st.error("PDF processing requires PyPDF2. Install: `pip install PyPDF2`")
                            st.stop()
                    
                    elif uploaded_file.type == "text/plain" or uploaded_file.name.endswith('.txt'):
                        # Read text file
                        with open(tmp_path, 'r', encoding='utf-8') as file:
                            extracted_text = file.read()
                    
                    # Show extracted content preview
                    if extracted_text:
                        char_count = len(extracted_text)
                        word_count = len(extracted_text.split())
                        
                        st.markdown("---")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Characters", f"{char_count:,}")
                        with col2:
                            st.metric("Words", f"{word_count:,}")
                        with col3:
                            st.metric("Estimated Pages", f"{word_count//500 + 1}")
                        
                        # Show preview
                        with st.expander("📖 Preview Extracted Content (First 1000 chars)"):
                            st.text(extracted_text[:1000] + "..." if len(extracted_text) > 1000 else extracted_text)
                        
                        # AI Analysis and Summarization
                        if OLLAMA_RUNNING:
                            st.markdown("### 🤖 AI Analysis & Summary")
                            
                            with st.spinner("Generating AI summary..."):
                                try:
                                    # Create summary prompt
                                    summary_prompt = f"""
                                    Analyze this educational content and provide a {summary_type.lower()} summary.
                                    
                                    CONTENT TYPE: {file_type} file
                                    TARGET AUDIENCE: {target_audience} level
                                    DETAIL LEVEL: {detail_level}/10
                                    FOCUS AREAS: {', '.join(focus_areas)}
                                    INCLUDE EXAMPLES: {'Yes' if include_examples else 'No'}
                                    
                                    CONTENT (first 4000 chars):
                                    {extracted_text[:4000]}
                                    
                                    Please provide:
                                    1. **Main Topic/Subject**
                                    2. **Key Concepts** (bullet points)
                                    3. **{summary_type} Summary**
                                    4. **Study Recommendations**
                                    
                                    Format the response clearly for educational purposes.
                                    """
                                    
                                    response = ollama.generate(
                                        model="gemma:2b",
                                        prompt=summary_prompt,
                                        options={'num_predict': 1000}
                                    )
                                    
                                    # Display AI summary
                                    st.markdown("### 📝 Generated Summary")
                                    st.markdown(response['response'])
                                    
                                    # Additional features
                                    st.markdown("---")
                                    col1, col2 = st.columns(2)
                                    
                                    with col1:
                                        if st.button("🧠 Generate Study Questions"):
                                            with st.spinner("Creating study questions..."):
                                                question_prompt = f"""
                                                Based on this content, create 5 study questions:
                                                
                                                Content summary: {response['response'][:500]}
                                                
                                                Create questions suitable for {target_audience} students.
                                                Include multiple choice questions with answers.
                                                """
                                                
                                                questions_resp = ollama.generate(
                                                    model="gemma:2b",
                                                    prompt=question_prompt,
                                                    options={'num_predict': 500}
                                                )
                                                st.markdown("### ❓ Study Questions")
                                                st.markdown(questions_resp['response'])
                                    
                                    with col2:
                                        if st.button("📚 Create Flashcards"):
                                            with st.spinner("Generating flashcards..."):
                                                flashcard_prompt = f"""
                                                Create 10 flashcards from this content:
                                                
                                                {response['response'][:300]}
                                                
                                                Format: Front (Question) | Back (Answer)
                                                Keep terms and definitions concise.
                                                """
                                                
                                                flashcards = ollama.generate(
                                                    model="gemma:2b",
                                                    prompt=flashcard_prompt,
                                                    options={'num_predict': 400}
                                                )
                                                st.markdown("### 🗂️ Flashcards")
                                                st.markdown(flashcards['response'])
                                    
                                    # Download options
                                    st.markdown("---")
                                    st.subheader("📥 Download Options")
                                    
                                    col1, col2 = st.columns(2)
                                    with col1:
                                        # Add datetime import at top of file first
                                        from datetime import datetime
                                        if st.button("💾 Save Summary as Text"):
                                            # Create downloadable text file
                                            summary_text = f"""
                                            PDF Summary Report
                                            ==================
                                            File: {uploaded_file.name}
                                            Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
                                            
                                            {response['response']}
                                            """
                                            
                                            st.download_button(
                                                label="Download Text Summary",
                                                data=summary_text,
                                                file_name=f"summary_{uploaded_file.name.split('.')[0]}.txt",
                                                mime="text/plain"
                                            )
                                    
                                    st.success("✅ Analysis complete!")
                                    
                                except Exception as ai_error:
                                    st.error(f"AI Analysis Error: {ai_error}")
                        else:
                            st.warning("🤖 Ollama not running. Enable AI for summarization features.")
                            st.info("Showing extracted text only:")
                            st.text_area("📄 Extracted Content", extracted_text[:3000], height=300)
                    
                    else:
                        st.error("⚠️ Could not extract text from the file.")
                    
                    # Cleanup
                    os.unlink(tmp_path)
                    
                except Exception as e:
                    st.error(f"❌ Processing Error: {e}")
                    import traceback
                    st.code(traceback.format_exc())
    else:
        st.info("👆 Upload a PDF or text file to begin analysis")
        
        # Show sample analysis
        with st.expander("📋 See Sample Analysis"):
            st.markdown("""
            **Sample PDF Analysis:**
            
            **Main Topic:** Introduction to Python Programming
            
            **Key Concepts:**
            - Variables and data types
            - Control structures (if/else, loops)
            - Functions and modules
            - File handling
            
            **Summary:**
            This introductory chapter covers Python basics suitable for beginners...
            
            **Study Recommendations:**
            1. Practice variable declaration
            2. Write simple programs
            3. Review control flow examples
            """)
# ==================== TAB 4: QUIZ GENERATOR ====================
# ==================== HELPER FUNCTIONS ====================
def parse_quiz_questions(quiz_text, num_questions):
    """Parse quiz text into structured questions - SIMPLIFIED VERSION"""
    questions = []
    lines = quiz_text.strip().split('\n')
    
    current_q = {}
    in_question = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Start of a new question
        if line.lower().startswith('q') and ('.' in line or ':' in line):
            if current_q and 'question' in current_q:
                questions.append(current_q)
                if len(questions) >= num_questions:
                    break
            
            # Extract question number and text
            if '.' in line:
                parts = line.split('.', 1)
                current_q = {
                    'question': parts[1].strip() if len(parts) > 1 else line,
                    'options': [],
                    'correct_answer': 'A',  # Default
                    'explanation': 'No explanation provided'
                }
            elif ':' in line:
                parts = line.split(':', 1)
                current_q = {
                    'question': parts[1].strip() if len(parts) > 1 else line,
                    'options': [],
                    'correct_answer': 'A',
                    'explanation': 'No explanation provided'
                }
            in_question = True
            
        # Options detection
        elif in_question and ('option' in line.lower() or 'choice' in line.lower() or 
                             line.startswith(('A)', 'B)', 'C)', 'D)', 'a)', 'b)', 'c)', 'd)'))):
            if ':' in line and ('option' in line.lower() or 'choice' in line.lower()):
                opts = line.split(':', 1)[1].strip()
                current_q['options'] = [opt.strip() for opt in opts.split(',')]
            elif line.startswith(('A)', 'B)', 'C)', 'D)', 'a)', 'b)', 'c)', 'd)')):
                current_q['options'].append(line)
                
        # Correct answer
        elif in_question and ('correct' in line.lower() or 'answer:' in line.lower()):
            if ':' in line:
                current_q['correct_answer'] = line.split(':', 1)[1].strip().upper()
            else:
                current_q['correct_answer'] = line.upper()
                
        # Explanation
        elif in_question and ('explanation:' in line.lower() or 'explain:' in line.lower()):
            if ':' in line:
                current_q['explanation'] = line.split(':', 1)[1].strip()
    
    # Add the last question
    if current_q and 'question' in current_q and len(questions) < num_questions:
        questions.append(current_q)
    
    # Fill in missing questions if needed
    while len(questions) < num_questions:
        questions.append({
            'question': f"Question {len(questions) + 1} about the topic",
            'options': ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
            'correct_answer': "A",
            'explanation': "This is a sample question."
        })
    
    return questions[:num_questions]
# ==================== TAB 4: QUIZ GENERATOR ====================
with tab4:
    st.subheader("🎯 Quiz Generator")
    
    # Initialize session state
    if 'quiz_generated' not in st.session_state:
        st.session_state.quiz_generated = False
    if 'current_quiz' not in st.session_state:
        st.session_state.current_quiz = None
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False

    # Quiz creation form
    with st.form("quiz_creation"):
        col1, col2 = st.columns(2)
        
        with col1:
            topic = st.text_input(
                "📚 Quiz Topic:",
                placeholder="e.g., Python, Cells, Gravity",
                key="quiz_topic_input"
            )
        
        with col2:
            qtype = st.selectbox(
                "🎮 Question Type:",
                ["Multiple Choice", "True/False"],
                key="quiz_type_select"
            )
        
        col3, col4 = st.columns(2)
        with col3:
            num_q = st.slider("📊 Questions:", 1, 10, 5, key="num_q_slider")
        
        with col4:
            difficulty = st.selectbox(
                "🎯 Difficulty:",
                ["Easy", "Medium", "Hard"],
                key="difficulty_select"
            )
        
        generate = st.form_submit_button("🚀 Generate Quiz", type="primary")
    
    # Generate quiz
    if generate and topic:
        if not OLLAMA_RUNNING:
            st.warning("⚠️ Ollama not running! Start it in AI Tutor tab first.")
        else:
            with st.spinner(f"Creating {difficulty} quiz about {topic}..."):
                try:
                    prompt = f"Create a {difficulty.lower()} {qtype.lower()} quiz about {topic} with {num_q} questions. Include questions, options, correct answers, and explanations."
                    
                    response = ollama.generate(
                        model="gemma:2b",
                        prompt=prompt,
                        options={'num_predict': 500}
                    )
                    
                    # Parse questions
                    questions = parse_quiz_questions(response['response'], num_q)
                    
                    # Store in session state
                    st.session_state.current_quiz = {
                        'topic': topic,
                        'type': qtype,
                        'difficulty': difficulty,
                        'questions': questions
                    }
                    
                    st.session_state.quiz_generated = True
                    st.session_state.user_answers = {}
                    st.session_state.show_results = False
                    
                    st.success(f"✅ Quiz generated! Answer the questions below.")
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Display quiz if generated
    if st.session_state.quiz_generated and st.session_state.current_quiz:
        quiz = st.session_state.current_quiz
        
        st.markdown("---")
        st.subheader(f"📝 {quiz['difficulty']} Quiz: {quiz['topic']}")
        
        # Display questions
        for i, q in enumerate(quiz['questions']):
            st.markdown(f"**Q{i+1}. {q['question']}**")
            
            # Show options
            if quiz['type'] == "Multiple Choice" and q.get('options'):
                for opt in q['options']:
                    st.write(f"  {opt}")
            
            # Answer input - Using radio to prevent refresh
            if quiz['type'] == "Multiple Choice":
                ans = st.radio(
                    f"Answer for Q{i+1}:",
                    ["Select...", "A", "B", "C", "D"],
                    key=f"ans_{i}",
                    horizontal=True,
                    index=0
                )
                if ans != "Select...":
                    st.session_state.user_answers[i] = ans
            else:  # True/False
                ans = st.radio(
                    f"Answer for Q{i+1}:",
                    ["Select...", "True", "False"],
                    key=f"ans_{i}",
                    horizontal=True,
                    index=0
                )
                if ans != "Select...":
                    st.session_state.user_answers[i] = ans
            
            st.markdown("---")
        
        # Submit button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📤 Submit Quiz", type="primary", key="submit_btn"):
                if st.session_state.user_answers:
                    # Calculate score
                    score = 0
                    total = len(quiz['questions'])
                    
                    for i, q in enumerate(quiz['questions']):
                        user_ans = st.session_state.user_answers.get(i, "")
                        correct_ans = q.get('correct_answer', 'A')
                        
                        if str(user_ans).upper() == str(correct_ans).upper():
                            score += 1
                    
                    # Store results
                    st.session_state.quiz_results = {
                        'score': score,
                        'total': total,
                        'percentage': (score/total)*100
                    }
                    st.session_state.show_results = True
                    st.success(f"✅ Submitted! Score: {score}/{total}")
                else:
                    st.warning("⚠️ Please answer at least one question!")
        
        # New quiz button
        if st.button("🔄 New Quiz", key="new_quiz"):
            st.session_state.quiz_generated = False
            st.session_state.current_quiz = None
            st.session_state.user_answers = {}
            st.session_state.show_results = False
            st.rerun()
    
    # Show results
    if st.session_state.get('show_results') and st.session_state.get('quiz_results'):
        results = st.session_state.quiz_results
        
        st.markdown("---")
        st.subheader("📊 Your Results")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Score", f"{results['score']}/{results['total']}")
        with col2:
            st.metric("Percentage", f"{results['percentage']:.1f}%")
        with col3:
            grade = "A+" if results['percentage'] >= 90 else "A" if results['percentage'] >= 80 else "B" if results['percentage'] >= 70 else "C" if results['percentage'] >= 60 else "D"
            st.metric("Grade", grade)
        
        # Performance message
        if results['percentage'] == 100:
            st.balloons()
            st.success("🎉 Perfect! Excellent work!")
        elif results['percentage'] >= 70:
            st.success("👍 Good job! Well done!")
        elif results['percentage'] >= 50:
            st.info("📚 Keep practicing!")
        else:
            st.warning("📖 Review and try again.")

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
