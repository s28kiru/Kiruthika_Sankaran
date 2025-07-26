from config import configure_gemini
from prompt_templates import (
    qa_prompt,
    glossary_prompt,
    step_guide_prompt,
    summarize_policy_prompt,
    ask_policy_question_prompt,
    search_augmented_prompt,
    call_script_prompt
)
from google_search import search_google_cse
from memory import get_memory_context


# Set up Gemini model
model = configure_gemini()

# ----------------------------
# Main executor for known intents
# ----------------------------
def execute(intent: str, goal: str) -> str:
    memory_context = get_memory_context()
    if intent == "qa":
        base_prompt = qa_prompt(goal)
    elif intent == "glossary":
        base_prompt = glossary_prompt(goal)
    elif intent == "step_guide":
        base_prompt = step_guide_prompt(goal)
    elif intent == "summarize_policy":
        base_prompt = summarize_policy_prompt(goal)
    elif intent == "call_script":
        base_prompt = call_script_prompt(goal)
    else:
        return "Sorry, I didn't understand your request."

    # Prepend memory context if available
    if memory_context:
        prompt = f"""
Here’s what the user has previously discussed with you:

{memory_context}

Now, address the following new question:

{base_prompt}
"""
    else:
        prompt = base_prompt

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"

# ----------------------------
# For uploaded policy + user question
# ----------------------------
def ask_about_uploaded_policy(policy_text: str, user_question: str) -> str:
    prompt = ask_policy_question_prompt(policy_text, user_question)
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"

# ----------------------------
# Google CSE + Gemini fallback
# ----------------------------
def execute_with_google_search(question: str) -> str:
    search_results = search_google_cse(question)

    if not search_results or "⚠️" in search_results[0]:
        return "\n".join(search_results)

    prompt = search_augmented_prompt(question, search_results)
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"

# ----------------------------
# Confidence checker utility
# ----------------------------
def is_low_confidence(response_text: str) -> bool:
    vague_phrases = [
        "depends on your plan",
        "you should contact your insurer",
        "may vary",
        "not sure",
        "unclear",
        "check with your provider",
        "cannot determine",
        "it is recommended to"
    ]
    return any(phrase in response_text.lower() for phrase in vague_phrases)
