# lapis_eye

A local AI agent that can use tools on your computer to complete tasks,
built from scratch to understand how AI agents really work.

Everything runs locally: your data never leaves your machine.

## Status

- [x] Phase 0: project setup
- [x] Phase 1: local LLM with Ollama
- [ ] Phase 2: tool calling (in progress)

See [ROADMAP.md](ROADMAP.md) for details.

## Tech stack

- Python 3.12
- Git / GitHub
- Ollama with `qwen3.5:2b-q4_K_M`

## Getting started

```powershell
# Create and activate the virtual environment (Windows)
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1

#Install the project dependencies
pip install -r requirements.txt
```
