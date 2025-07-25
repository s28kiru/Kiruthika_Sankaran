# src/app.py

import streamlit as st
from planner import plan
from executor import execute

st.set_page_config(page_title="🛡️ InsureMate", layout="centered")

st.title("🛡️ InsureMate: Your AI Insurance Copilot")
st.markdown(
    "Ask me anything about **health insurance**. "
    "I'll help you understand what's covered, what steps to take, and clarify confusing terms."
)

# User input box
user_input = st.text_area(
    "Enter your insurance question or scenario below:",
    placeholder="e.g., I got into a car accident. What do I do?",
    height=150
)

# Submit button
if st.button("Get Help"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing your request..."):
            # Step 1: Plan the task
            plan_result = plan(user_input)

            # Step 2: Run executor
            result = execute(plan_result["intent"], plan_result["goal"])

        # Step 3: Display result
        st.markdown("### ✅ Here's what I found:")
        st.write(result)

