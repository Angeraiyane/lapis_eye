# lapis_eye — Roadmap

A local AI agent that uses tools on the computer to complete tasks, built step by step to understand every part.

## Principles

- **Understand before moving on**: a phase is finished only when every line is understood.
- **From scratch first, frameworks second**: build the agent loop by hand before using LangGraph.
- **Local first**: the LLM runs on the machine (Ollama). Data never leaves the computer.
- **Security by design**: least privilege, human confirmation for risky actions, no secrets in Git.
- **Extensible tools**: every tool is an independent module plugged into a tool registry.
- **Budget**: free and open-source tools. 200 MAD kept in reserve for a cloud API fallback only if needed.

## Hardware

- Windows 11 Home, 16 GB RAM
- NVIDIA GTX 1650 Ti (4 GB VRAM), CUDA driver 13.0
- Target models: 3-4B parameters (fully on GPU); 7-8B possible with CPU offload (slower)

## Environment

- Dependencies: `requirements.txt` (`pip install -r requirements.txt`)
- Python 3.12.16 (Astral/uv-managed), virtual env in `.venv`
- Created with: `py -V:Astral\CPython3.12.16 -m venv .venv`
- Git branch `main`, remote `origin` on GitHub

## Model

- Engine: Ollama (local server on `http://localhost:11434`)
- Main model: `qwen3.5:2b-q4_K_M` (Apache 2.0, tools + thinking capabilities)
- Settings: `think: false`, `temperature: 0` (deterministic output)
- Benchmark (GTX 1650 Ti, Steam/Brave open):

| Variant | Size in memory | Processor | Generation speed |
|---|---|---|---|
| `qwen3.5:2b` (Q8_0, default tag) | 3.0 GB | 37%/63% CPU/GPU | ~20 tokens/s |
| `qwen3.5:2b-q4_K_M` | 1.6 GB | 100% GPU | ~60 tokens/s |

- Lessons: the default tag is not always the right one; CPU offload can divide speed by 3; first run includes a one-time warm-up.

## Phases

| Phase | Goal | Key skills |
|---|---|---|
| 0. Foundations | Environment, Git, GitHub, project structure | venv, uv, Git, Markdown |
| 1. Local LLM | Install Ollama, pick a tool-calling model, call its HTTP API | LLM basics, tokens, quantization, REST APIs |
| 2. Tool calling by hand | Define first tools (read file, list directory) with JSON Schema; build the tool registry | Function calling, JSON Schema |
| 3. Agent loop from scratch | Implement the ReAct loop without any framework | Reason + Act, message history |
| 4. Powerful tools + security | Shell commands, web search, human confirmation, allowlists, limits | Sandboxing, least privilege |
| 5. Memory | Conversation history, context summarization, SQLite, RAG (embeddings + vector store) | Context window, semantic search |
| 6. Market tools | Rebuild with LangGraph; expose tools through MCP | Frameworks vs hand-made |
| 7. Interface | CLI, then FastAPI backend + Streamlit UI | Client/server architecture |
| 8. Production-ready | Tests (pytest), logging, Docker, documentation | Industrialization, portfolio |

## Progress

- [x] Phase 0 — Foundations
- [x] Phase 1 — Local LLM
- [ ] Phase 2 — Tool calling by hand (in progress)
- [ ] Phase 3 — Agent loop from scratch
- [ ] Phase 4 — Powerful tools + security
- [ ] Phase 5 — Memory
- [ ] Phase 6 — Market tools
- [ ] Phase 7 — Interface
- [ ] Phase 8 — Production-ready