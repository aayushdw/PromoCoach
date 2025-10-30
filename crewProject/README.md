# PromoCoach - CrewAI Version

AI-powered career development assistant built with CrewAI and CrewAI Flows.

## Features

- **Competency Analysis**: Analyzes company leveling documents
- **Gap Analysis**: Identifies gaps between current and target levels
- **Opportunity Finder**: Finds learning courses and project opportunities
- **Promotion Package Builder**: Creates professional promotion documents

## Setup

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Configure Environment**:
```bash
cp .env.template .env
# Edit .env and add your GEMINI_API_KEY
```

3. **Prepare Data**:
- Add your input files to the `data/` directory
- Files should be in `.txt` format (see data folder for examples)

## Running

```bash
# Normal mode
python main.py

# Test mode (skips prompts, uses saved info)
TEST_MODE=true python main.py
```

## Project Structure

```
crewProject/
├── agents/          # CrewAI agents
├── tasks/           # CrewAI tasks
├── tools/           # CrewAI tools (if needed)
├── flows/           # CrewAI flows
├── data/            # Input data files
├── outputs/         # Generated outputs
├── state.py         # State management
├── main.py          # Entry point
└── requirements.txt # Dependencies
```

## Differences from LangGraph Version

- Uses CrewAI agents with roles and backstories
- Uses CrewAI flows for orchestration
- Simpler state management with Pydantic
- Built-in memory through CrewAI's context system

## Notes

- This is a simplified translation from LangGraph
- State is managed through the Flow class
- Guardrails are handled by CrewAI's built-in validation
- Memory is maintained through CrewAI's context passing

