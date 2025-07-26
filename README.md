# 🛡️ InsureMate — Your AI-Powered Insurance Navigator

**InsureMate** is a conversational insurance assistant that helps users understand policies, define confusing terms, generate insurer call scripts, summarize documents, and get real-time answers using AI + web search — all through a clean Streamlit UI.

---

## 🚀 Live Demo

Try it now →  
**🔗 https://kiruthikasankaran-insuremate-agent.streamlit.app/**

> ✅ Deployed using [Streamlit Cloud](https://streamlit.io/cloud)  
> ✅ No local setup required  
> 🔐 Secrets (API keys) securely managed via Streamlit Secrets

---

## 🧰 Features

- 💬 Ask insurance-related questions in plain English  
- 📖 Define terms like deductible, copay, coinsurance  
- 📄 Upload and summarize insurance policies  
- 📞 Generate call scripts for tricky situations like denial or appeal  
- 🌐 Get real-time answers using Google search  
- 🧠 Session memory helps maintain context in follow-up questions  

---

## ⚙️ How It Was Set Up (No Local Install Needed)

1. Code pushed to **GitHub**
2. Connected GitHub repo to **Streamlit Cloud**
3. Added required API keys in **Streamlit → App → Settings → Secrets**
4. Streamlit auto-deployed and hosted the app

---

## 🔐 Required Secrets

Set these in Streamlit under **App → Settings → Secrets**:

```toml
GOOGLE_API_KEY = "your_google_generative_ai_key"
CSE_API_KEY = "your_google_custom_search_api_key"
CSE_ID = "your_custom_search_engine_id"
```

* GOOGLE_API_KEY: Get from https://makersuite.google.com/app/apikey

* CSE_API_KEY + CSE_ID: Get from https://programmablesearchengine.google.com

## Project Structure

src/
├── app.py                # Streamlit app frontend
├── config.py             # Gemini and secrets loader
├── executor.py           # Task executor logic
├── planner.py            # Maps user input to intent
├── prompt_templates.py   # Prompt generator functions
├── memory.py             # Session memory logic
├── google_search.py      # Google CSE integration
├── utils.py              # Formatters and helpers
├── requirements.txt      # Python dependencies
└── .streamlit/
    └── secrets.toml      # (set in Streamlit Cloud UI, not stored in GitHub)

