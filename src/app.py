# src/app.py

import streamlit as st
from planner import plan
from executor import (
    execute,
    execute_with_google_search,
    is_low_confidence,
    ask_about_uploaded_policy
)
from utils import extract_text_from_pdf
from memory import init_memory, log_memory


# ---- App Config ----
st.set_page_config(page_title="🛡️ InsureMate", layout="centered")
init_memory()


st.title("🛡️ InsureMate: Your AI Insurance Copilot")
st.markdown(
    "Ask me anything about **health insurance**. "
    "I'll help you understand what's covered, what steps to take, and clarify confusing terms."
)

# ---- User Input ----
user_input = st.text_area(
    "Enter your insurance question or scenario below:",
    placeholder="e.g., I got into a car accident. What do I do?",
    height=150
)

# ---- Submit Button ----
if st.button("Get Help"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing your request..."):
            plan_result = plan(user_input)
            intent = plan_result["intent"]
            goal = plan_result["goal"]

            if intent in ["qa", "glossary", "step_guide", "summarize_policy"]:
                response = execute(intent, goal)

                if is_low_confidence(response):
                    st.info("The AI wasn't confident — checking the web for better info...")
                    response = execute_with_search(user_input)
                    st.markdown("### 🌐 Web-augmented Answer (Fallback):")
                else:
                    st.markdown("### ✅ Agent Answer:")
            else:
                st.info("Looks like a very specific question — using web search...")
                response = execute_with_google_search(user_input)
                st.markdown("### 🌐 Web-augmented Answer:")

        st.write(response, unsafe_allow_html=True)
        log_memory(user_input, result)


# ---- Document Upload Section ----
st.markdown("---")
st.markdown("### 📁 Ask a question about a full policy document")

uploaded_file = st.file_uploader("Upload your insurance policy (PDF or TXT)", type=["pdf", "txt"])
policy_question = st.text_input("Ask a question about this document", placeholder="e.g., Does it cover ambulance services?")

if st.button("Ask About Uploaded Policy"):
    if not uploaded_file or not policy_question.strip():
        st.warning("Please upload a file and ask a question.")
    else:
        with st.spinner("Reading your policy and analyzing..."):
            # Read and extract text
            if uploaded_file.type == "application/pdf":
                policy_text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.type == "text/plain":
                policy_text = uploaded_file.read().decode("utf-8")
            else:
                st.error("Unsupported file type")
                policy_text = ""

            if policy_text:
                result = ask_about_uploaded_policy(policy_text, policy_question)
                st.markdown("### 📋 Answer Based on Uploaded Policy:")
                st.write(result, unsafe_allow_html=True)

