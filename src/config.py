import os
import google.generativeai as genai

def configure_gemini():
    # Get API key from Streamlit secrets or .env
    api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("Gemini API key not found. Please set GEMINI_API_KEY in environment or Streamlit secrets.")
    
    genai.configure(api_key=api_key)

    # Return Gemini Pro model
    return genai.GenerativeModel("gemini-pro")
