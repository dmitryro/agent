# app.py
import streamlit as st
from fuzzywuzzy import fuzz

# Hardcoded dataset
DATASET = {
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}

# Function to find the most relevant answer
def find_relevant_answer(user_input):
    best_match = None
    highest_score = 0
    
    for item in DATASET["questions"]:
        score = fuzz.partial_ratio(user_input.lower(), item["question"].lower())
        if score > highest_score and score > 70:  # Threshold for relevance
            highest_score = score
            best_match = item["answer"]
    
    if best_match:
        return best_match
    else:
        # Fallback to generic response
        return "I'm sorry, I don't have specific information about that. Could you please rephrase or ask another question about Thoughtful AI's agents?"

# Streamlit UI
def main():
    st.set_page_config(page_title="Thoughtful AI Customer Support", page_icon="🤖")
    
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
        }
        .stTextInput > div > div > input {
            border: 2px solid #0066cc;
            border-radius: 5px;
        }
        .stButton > button {
            background-color: #0066cc;
            color: white;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🤖 Thoughtful AI Customer Support Agent")
    st.write("Ask me anything about Thoughtful AI's agents!")
    
    # Initialize session state for conversation history
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    # Input form
    with st.form(key='question_form', clear_on_submit=True):
        user_input = st.text_input("Your Question:", placeholder="e.g., What does EVA do?")
        submit_button = st.form_submit_button("Ask")
    
    # Process question
    if submit_button and user_input:
        if len(user_input.strip()) < 3:
            st.error("Please enter a valid question (at least 3 characters).")
        else:
            answer = find_relevant_answer(user_input)
            st.session_state.history.append({"question": user_input, "answer": answer})
            
            # Display latest response
            st.success("Answer:")
            st.write(answer)
    
    # Display conversation history
    if st.session_state.history:
        st.markdown("---")
        st.subheader("Conversation History")
        for i, entry in enumerate(reversed(st.session_state.history[-5:]), 1):  # Show last 5 exchanges
            st.markdown(f"**Q{i}:** {entry['question']}")
            st.markdown(f"**A{i}:** {entry['answer']}")
            st.markdown("---")

if __name__ == "__main__":
    main()
