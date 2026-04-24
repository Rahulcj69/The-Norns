# The Norns

The Norns is a local AI-powered learning system built on a multi-agent temporal intelligence architecture. It is designed to improve student learning outcomes by combining historical analysis, real-time reasoning, and future optimization.

## Core Idea

The system is inspired by the three Norns of Norse mythology:

- Urd (Past): analyzes historical student data
- Verdandi (Present): handles real-time queries and interactions
- Skuld (Future): generates recommendations and optimizations

These three engines work together to produce a unified output layer referred to as "The Norns".

## Architecture

User Input → Verdandi → Urd + Context → Skuld → Final Output

## Components

### Urd (Past Engine)
- Tracks student performance
- Identifies weak and strong topics
- Detects repeated mistakes and patterns

### Verdandi (Present Engine)
- Handles user queries in real time
- Uses a local LLM (Gemma via Ollama)
- Provides immediate responses

### Skuld (Future Engine)
- Generates recommendations
- Suggests study plans
- Optimizes learning paths based on past and present data

## Current Status

- Local LLM integration completed (Ollama + Gemma)
- Basic query handling implemented (Verdandi)
- System architecture defined

## Tech Stack

- Python
- Ollama (Gemma models)
- Requests (API communication)

## Setup

1. Install dependencies:
   pip install requests

2. Run Ollama:
   ollama run gemma4:e2b

3. Run the system:
   python main.py

## Vision

To build a structured, self-improving AI learning system that combines data-driven analysis with LLM-assisted reasoning, rather than relying on raw language model outputs alone.

## Author

Rahul Mandyal