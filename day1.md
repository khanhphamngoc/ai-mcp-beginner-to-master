# Day 1 – MCP Fundamentals

## What is MCP?
The Model Context Protocol is a standardized way to give models (like GPT-4 or Claude) context — not just in a single prompt, but across multiple turns, tools, threads, and agents.

🧩 Think of MCP as giving your agent a brain + memory — not just chat history.

## Why does it matter?
| Without MCP                  | With MCP                              |
| ---------------------------- | ------------------------------------- |
| Stateless, no memory         | Persistent memory across turns        |
| Prompt hacking for structure | Native schema support                 |
| Hard to evolve conversations | Thread evolution + tool state         |
| Agents forget users          | Agents "remember" goals, tasks, roles |


## Key Components

| Component | Description |
|-----------|---------------------------------------------------------------|
| Thread    | Represents a single ongoing conversation or task              |
| Message   | A user or model statement within a thread                     |
| Context   | Any information (history, instructions, tools) that helps the model reason |
| Role      | Who authored the message: user, assistant, tool               |
| Tool use  | The model asks for or invokes external functions              |
| Schema    | Defines how structured data is passed in and out              |

## How I think about it:
(Make your own analogy or example here)

## Diagram (optional)
Use Mermaid.js to draw the architecture below.
mermaid
    sequenceDiagram
        participant User
        participant Thread
        participant MCP
        participant Model

        User->>Thread: Add message
        Thread->>MCP: Build context (history, tools, schema)
        MCP->>Model: Send prompt with context
        Model-->>MCP: Reply or Tool Call
        MCP->>Thread: Append model response

## Shared Thread in MCP

In MCP, a **Thread** represents the entire conversation or task history. When multiple agents (with different roles) work together on the same task, they can:

- **Read from the same thread** → Get shared context
- **Append messages to the same thread** → Contribute their own reasoning
- **See each other's tool calls, summaries, or decisions**  
  → Enabling coordination, not just isolated responses.

This is critical for agent collaboration, especially in systems like:

- Multi-agent copilots (researcher + planner + executor)
- Customer onboarding (bot + verifier + escalation assistant)
- Enterprise workflows (data collector + analyzer + reporter)

| Agent Role            | Function                               | Message Type              |
| --------------------- | -------------------------------------- | ------------------------- |
| `user`                | Initiates request or feedback          | user message              |
| `researcher`          | Gathers raw info                       | assistant message         |
| `planner`             | Creates structured output from info    | assistant message         |
| `executor`            | Takes final action (API call, summary) | tool use / final response |
| `reviewer` (optional) | Evaluates previous agents' work        | assistant message         |
### Benefits of the Shared Thread Model

- Collective reasoning: Agents build on each other’s logic
- Context continuity: Nothing is lost between agents
- Auditability: Easy to debug or explain each step
- Tool chaining: One agent can prep data, another can use it in a tool

