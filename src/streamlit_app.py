import streamlit as st
import sys
import os

# Add src to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

st.set_page_config(page_title="Educational Assistant", layout="wide")
st.title("🎓 Educational Content Assistant")

# Import your existing functionality
from educational_assistant import KnowledgeBase

# Initialize knowledge base
@st.cache_resource
def init_kb():
    kb = KnowledgeBase()
    kb.load_courses()
    return kb

kb = init_kb()

# UI Components
st.sidebar.header("Settings")
course_option = st.sidebar.selectbox("Select Course", ["Biology", "Computer Science"])

st.header("Ask Questions")
question = st.text_input("Enter your question about the course:")

if st.button("Get Answer") and question:
    with st.spinner("Searching for answer..."):
        # Use your existing KnowledgeBase methods
        results = kb.search(question, max_results=3)
        
        st.subheader("Answer:")
        
        if not results:
            st.warning("No results found. Try a different question.")
        else:
            for i, result in enumerate(results, 1):
                # Extract content from the result dictionary
                content = result.get('content', 'No content')
                score = result.get('score', 0)
                source = result.get('source', 'Unknown')
                
                st.markdown(f"**🔍 Result {i}** (Relevance: {score}/5)")
                st.markdown(f"**Content:** {content}")
                st.markdown(f"**Source:** `{source}`")
                st.markdown("---")
        
        st.success("✅ Answer retrieved!")

st.markdown("---")
st.info("This is a Streamlit wrapper around your existing RAG system.")
