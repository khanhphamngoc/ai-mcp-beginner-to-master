# Day 3 - Multi-Turn Memory & Context Summarization

## Objectives

Enable agent to:
- Store and manage long-term memory (multiple user sessions)
- Summarize past threads so future responses stay efficient and context-aware

## Why This Matters
As conversations grow, feeding the entire history into the LLM becomes:
- Expensive (if using tokens)
- Inefficient (if many irrelevant details)
- Confusing (if repetition or irrelevant turns)

🔁 Summarization lets the agent condense knowledge and continue reasoning without losing important signals.

