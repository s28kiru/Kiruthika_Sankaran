def plan(user_input: str) -> dict:
    input_lower = user_input.lower().strip()

    # Glossary terms: definitions, meanings
    glossary_keywords = ["what is", "define", "meaning of", "explain", "term"]
    if any(kw in input_lower for kw in glossary_keywords):
        return {
            "intent": "glossary",
            "goal": user_input.strip()
        }

    # Summary-type input: asking to summarize policy or coverage
    summary_keywords = [
        "summarize", 
        "simplify", 
        "can you read", 
        "understand this policy", 
        "translate", 
        "explain this policy",
        "help me understand this coverage"
    ]
    if any(kw in input_lower for kw in summary_keywords) or len(user_input.split()) > 100:
        return {
            "intent": "summarize_policy",
            "goal": user_input.strip()
        }

    # Step-by-step guidance: What to do next, situations
    scenario_keywords = [
        "accident", "hospital", "got", "was admitted", "file a claim", 
        "stolen", "hit", "crash", "what to do", "what do i do", "next steps", 
        "what should i do", "process for", "how to proceed"
    ]
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
