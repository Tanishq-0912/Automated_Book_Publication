# README.md
# Automated Book Publication Workflow

## Objective
Create a system to fetch content from a web URL, apply AI-driven transformations to chapters, and allow multiple human-in-the-loop review iterations, all orchestrated with reward-based feedback and semantic search.

## Features
- Web scraping and screenshot of chapter content
- AI-generated "spun" text using an LLM
- AI-powered review for grammar, clarity, and tone
- Reinforcement learning-style reward scoring
- Versioning and semantic search using ChromaDB
- Voice support for reading drafts aloud
- Human-in-the-loop workflow for accepting, revising, or rejecting outputs

## Tech Stack
- Python
- Playwright (scraping)
- OpenAI API (AI writer and reviewer)
- ChromaDB (semantic search & versioning)
- pyttsx3 (voice interface)

## Run Instructions
```bash
# Install dependencies
pip install -r requirements.txt

# Download browser binaries for Playwright
playwright install

# Run the workflow
python main.py
```
