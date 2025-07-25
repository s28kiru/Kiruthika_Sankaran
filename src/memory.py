import streamlit as st

# Store the last N messages in session memory
MAX_MEMORY = 5

def init_memory():
    if "chat_memory" not in st.session_state:
        st.session_state.chat_memory = []

def log_memory(user_input: str, agent_response: str):
    st.session_state.chat_memory.append({
        "user": user_input,
        "agent": agent_response
    })
    # Keep only last N items
    st.session_state.chat_memory = st.session_state.chat_memory[-MAX_MEMORY:]

def get_memory_context() -> str:
    if "chat_memory" not in st.session_state or not st.session_state.chat_memory:
        return ""
    
    context = "\n\n".join(
        [f"User: {item['user']}\nAgent: {item['agent']}" for item in st.session_state.chat_memory]
    )
    return context
