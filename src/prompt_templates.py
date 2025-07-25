# src/prompt_templates.py

def qa_prompt(question: str) -> str:
    return f"""
You are an expert insurance assistant. The user asked: "{question}"

Respond with:
1. A plain-English explanation of the situation.
2. What is typically covered under insurance.
3. Actionable next steps the user should take (if applicable).
4. Definitions of any insurance terms used.

Be brief, practical, and clear. Write like you're helping a confused friend.
"""


def glossary_prompt(term: str) -> str:
    return f"""
Explain the insurance term "{term}" in simple, friendly language.

Include:
- A definition
- A real-life example
- When this term matters to someone using insurance

Avoid jargon. Keep it under 200 words.
"""


def step_guide_prompt(scenario: str) -> str:
    return f"""
A user is describing this scenario: "{scenario}"

You are an insurance agent helping them respond to this situation.

Generate a numbered, step-by-step guide:
1. What should they do first?
2. What should they prepare (documents, claims)?
3. Who should they call?
4. What terms might apply in this case?

Write calmly and clearly, as if guiding someone in a stressful moment.
"""
