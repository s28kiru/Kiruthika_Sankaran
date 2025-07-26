# Technical Explanation

# InsureMate Technical Explanation

This document describes how **InsureMate**, the AI insurance navigator, processes inputs, manages memory, integrates external tools, and handles edge cases. It follows a modular design for clarity, extensibility, and maintainability.

---

## 1. 🧭 Agent Workflow

Step-by-step overview of how the agent processes user input:

### 1. Receive User Input
The user interacts with a **Streamlit UI** (via `app.py`), which captures the natural language question or task.

### 2. (Optional) Retrieve Relevant Memory
The agent loads session-level memory via `memory.py` to provide context-aware responses. This includes prior questions, uploaded policies, or conversation goals.

### 3. Plan Sub-tasks
`planner.py` decides which **intent** applies (e.g., `qa`, `glossary`, `step_guide`, `summarize_policy`, etc.). It then selects the appropriate **prompt** from `prompt_templates.py`.

### 4. Call Tools or APIs
Based on the plan:
- Gemini API is used for reasoning and generation (`config.py`)
- Google CSE is used for search-augmented answers (`google_search.py`)
- Memory context is added as part of the prompt construction

### 5. Summarize and Return Final Output
`executor.py` assembles the result and returns it to the Streamlit frontend. The output may include a direct answer, glossary term, steps, or a summary — along with relevant links or disclaimers.

---

## 2. 🔑 Key Modules

### `app.py`
- Streamlit-based UI interface
- Routes user input to the planner/executor pipeline
- Displays results and optional debug/log information

### `planner.py`
- Maps user input (or intent selector) to agent intent
- Chooses the appropriate prompt and tools to invoke
- Coordinates prompt construction using `prompt_templates.py`

### `executor.py`
- Orchestrates end-to-end reasoning
- Calls Gemini via `config.py` or invokes search tools
- Combines memory, goal, and intent for final output

### `memory.py`
- Session-based memory manager
- Retrieves prior context (e.g., uploaded policy, previous goal)
- Memory is currently ephemeral and not persisted

### `prompt_templates.py`
- Contains all prompt templates (qa, glossary, step guide, etc.)
- Modular design enables quick updates for new intents

### `google_search.py`
- Interfaces with **Google Programmable Search Engine**
- Called for search-augmented prompts
- Returns top search results for grounding responses

### `config.py`
- Configures the Gemini API
- Loads API keys and generation parameters from environment variables

### `utils.py`
- Shared utilities (e.g., formatting, error handling, helper functions)

---

## 3. 🔌 Tool Integration

| Tool | Purpose | Call Format |
|------|---------|-------------|
| **Gemini API** | Core reasoning/generation | `model.generate_content(prompt)` via `config.py` |
| **Google Search (CSE)** | Real-time search | `search_google_cse(query)` from `google_search.py` |
| **Prompt Templates** | Task-specific prompting | `qa_prompt(goal)`, `step_guide_prompt(goal)`, etc. |

---

## 4. 🔍 Observability & Testing

### Logging
- Optionally printed to Streamlit sidebar for debugging
- Logs can be extended to save in `logs/` directory via `utils.py`

### Testing
- Add test cases in `tests/test_executor.py` or `TEST.sh`
- Test coverage should include all major intents with and without memory context
- Use mocked LLM responses to test fallback logic

---

## 5. ⚠️ Known Limitations

| Limitation | Notes |
|------------|-------|
| **No Persistent Memory** | Memory resets on session end. Future support for DB/VectorStore planned. |
| **Static Intent Routing** | Currently rule-based. No dynamic intent classification yet. |
| **Ambiguous Input Handling** | User may need to explicitly select intent when unclear. |
| **LLM Hallucination Risk** | Gemini may output plausible but inaccurate information if search is not used. |
| **Long-running LLM Calls** | Large prompts may introduce latency. |
| **No API-based Quote Integration** | Real insurer quote retrieval not yet implemented. |

---

InsureMate is modular, lightweight, and easy to extend. Its architecture is optimized for transparent decision-making, integration with external tools, and clear conversational assistance via a friendly web interface.

