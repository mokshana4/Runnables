# LangChain Runnables and Agents

This repository contains hands-on implementations of LangChain Runnables, Tools, and Agents using Python. The project explores how complex AI workflows can be built by chaining multiple operations, executing tasks in parallel, creating custom tools, and enabling Large Language Models (LLMs) to interact with external functionalities.

The primary goal of this repository is to understand the execution flow of LangChain applications and learn how agents use reasoning and tool-calling capabilities to solve tasks dynamically.

---

## Concepts Explored

* LangChain Runnables
* Runnable Sequences
* Runnable Parallel Execution
* Runnable Passthrough
* Tool Calling
* Custom Tools
* AI Agents
* Agent Creation and Execution
* LLM-Orchestrated Workflows
* News Summarization
* Prompt Chaining

---

## Project Structure

```text
RUNNABLES/
│
├── Agents.py                   # Agent implementation examples
├── Create_Agents.py            # Agent creation workflows
├── sequencerunnable.py         # RunnableSequence examples
├── parallelrunnable.py         # RunnableParallel examples
├── runnablepassthrough.py      # RunnablePassthrough examples
├── toolcalling.py              # Tool calling implementation
├── owntool.py                  # Custom tool creation
├── newssummarizer.py           # News summarization workflow
│
├── .env                        # Environment variables (ignored by Git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## File Description

### Agents.py

Contains implementations of AI agents that use language models to reason, plan, and execute tasks.

### Create_Agents.py

Demonstrates how agents are created, configured, and connected with tools and language models.

### sequencerunnable.py

Explores `RunnableSequence`, where outputs from one step become inputs to the next step in a structured workflow.

### parallelrunnable.py

Demonstrates `RunnableParallel`, allowing multiple tasks to execute simultaneously and return combined results.

### runnablepassthrough.py

Explores `RunnablePassthrough`, which forwards data through a workflow while preserving original inputs.

### toolcalling.py

Shows how language models invoke tools dynamically to perform tasks beyond text generation.

### owntool.py

Implements custom tools that can be integrated into agent workflows.

### newssummarizer.py

A practical application that retrieves and summarizes news content using LLM-powered workflows.

---

## Technologies Used

* Python 3.x
* LangChain
* OpenAI API
* Groq API
* Google Gemini API
* python-dotenv

---

## Workflow Overview

1. User provides a query or task.
2. Runnable components process the input.
3. Tasks can be executed sequentially or in parallel.
4. Agents determine whether external tools are required.
5. Tools are invoked when necessary.
6. Results are collected and passed through the workflow.
7. The language model generates the final response.

---

## Purpose

This repository serves as a learning project for understanding LangChain's Runnable architecture and Agent framework. It demonstrates how AI applications can be built using sequential pipelines, parallel execution, custom tools, and intelligent agents capable of reasoning and task orchestration.
