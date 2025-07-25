def plan(user_input: str) -> dict:
    input_lower = user_input.lower().strip()

    # Rule: Glossary prompt if user is asking for definition
    glossary_keywords = ["what is", "define", "meaning of", "explain", "term"]
    if any(kw in input_lower for kw in glossary_keywords):
        return {
            "intent": "glossary",
            "goal": user_input.strip()
        }

    # Rule: Step-by-step guidance if action verbs are present
    scenario_keywords = ["accident", "hospital", "got", "was admitted", "file a claim", "stolen", "hit", "crash"]
    if any(kw in input_lower for kw in scenario_keywords):
        return {
            "intent": "step_guide",
            "goal": user_input.strip()
        }

    # Fallback: General insurance Q&A
    return {
        "intent": "qa",
        "goal": user_input.strip()
    }
