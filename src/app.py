# src/app.py

import streamlit as st

st.set_page_config(page_title="InsureMate", layout="centered")

st.title("InsureMate: Your AI Insurance Copilot")
st.markdown("Ask me anything about **health** insurance** — I’ll help you understand what’s covered and what to do next.")

# User input
user_input = st.text_area("Enter your insurance question or scenario below:", placeholder="e.g., I had to visit the ER — will insurance cover that?", height=150)

# Submit button
if st.button("Get Help"):
    if not user_input.strip():
        st.warning("Please enter a question or scenario.")
    else:
        st.info("Processing your request...")
        # We'll plug in planner → executor here
