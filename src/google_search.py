import requests
import os
import streamlit as st

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID") or st.secrets.get("GOOGLE_CSE_ID")

def search_google_cse(query: str, num_results: int = 3):
    if not GOOGLE_API_KEY or not GOOGLE_CSE_ID:
        return ["⚠️ Google CSE credentials missing."]
    
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": num_results
    }

    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        items = res.json().get("items", [])
    except Exception as e:
        return [f"⚠️ Google Search failed: {e}"]

    results = []
    for item in items:
        title = item.get("title")
        snippet = item.get("snippet")
        link = item.get("link")
        if title and snippet:
            results.append(f"**{title}**\n{snippet}\n🔗 {link}")
    return results if results else ["⚠️ No search results found."]
