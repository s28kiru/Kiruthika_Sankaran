from prompt_templates import qa_prompt, glossary_prompt, step_guide_prompt
from config import configure_gemini

# Set up the model
model = configure_gemini()

def execute(intent: str, goal: str) -> str:
    if intent == "qa":
        prompt = qa_prompt(goal)
    elif intent == "glossary":
        prompt = glossary_prompt(goal)
    elif intent == "step_guide":
        prompt = step_guide_prompt(goal)
    else:
        return "Sorry, I didn't understand your request."

    # Call Gemini and get the response
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"
