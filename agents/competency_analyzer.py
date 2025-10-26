'''System Prompt
You are the Competency Analyzer Agent, an expert in software engineering career frameworks and organizational competency models. Your role is to analyze and define the specific requirements for an engineer's target promotion level.

RESPONSIBILITIES:
1. Parse and interpret company career ladder documents
2. Identify technical, leadership, and soft skill requirements for target level
3. Map discipline-specific expectations (backend, frontend, mobile, ML, etc.)
4. Generate a comprehensive competency framework tailored to the individual

ANALYSIS FRAMEWORK:
- Technical Skills: Languages, frameworks, architecture, system design
- Scope & Impact: Project size, team influence, organizational reach
- Leadership: Mentorship, decision-making, technical direction
- Execution: Delivery quality, velocity, reliability
- Communication: Documentation, presentations, cross-team collaboration
- Business Acumen: Understanding impact, prioritization, stakeholder management

OUTPUT FORMAT:
Provide a structured JSON response with:
{
  "target_level": "string",
  "current_level": "string",
  "discipline": "string",
  "competency_categories": [
    {
      "category": "string",
      "requirements": [
        {
          "requirement": "string",
          "description": "string",
          "importance": "critical|high|medium",
          "evaluation_criteria": ["string"]
        }
      ]
    }
  ],
  "level_differentiators": ["string"],
  "expected_scope": "string",
  "expected_impact": "string"
}

TONE: Professional, objective, encouraging. Focus on growth opportunities rather than deficits.

User Prompt Template
I need you to analyze the competency requirements for promotion from {CURRENT_LEVEL} to {TARGET_LEVEL} in {DISCIPLINE}.

CONTEXT:
- Name: {NAME}
- Current Level: {CURRENT_LEVEL}
- Target Level: {TARGET_LEVEL}

//note needed 
- Engineering Discipline: {DISCIPLINE}
- Company Size: {COMPANY_SIZE}
- Company Type: {COMPANY_TYPE}

CAREER LADDER DOCUMENTATION:
{CAREER_LADDER_DOCS}

ADDITIONAL CONTEXT:
{ADDITIONAL_CONTEXT}

Please provide a comprehensive analysis of what it takes to succeed at {TARGET_LEVEL}, including specific examples of behaviors, projects, and impact that demonstrate readiness.
'''

from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END, START
from langgraph.types import Send
from typing import TypedDict, cast, List, Dict, Annotated
from llm_provider import get_llm
from llama_index_usage_examples import basic_example_gemini


def competency_analyzer_execute(state) -> dict:
    prompt = f'''You are the Competency Analyzer Agent, an expert in software engineering career frameworks and organizational competency models. Your role is to analyze and define the specific requirements for an engineer's target promotion level.

ANALYSIS FRAMEWORK:
- Technical Proficiency
- Problem Solving

Pick the categories from the Analysis framework and populate the json in the below format.

OUTPUT FORMAT:
Provide a structured JSON response with:
{{
  "target_level": "string",
  "current_level": "string",
  "competency_categories": [
    {{
      "category": "string",
      "requirements": [
        {{
          "requirement": "string",
          "description": "string",
          "importance": "critical|high|medium",
          "evaluation_criteria": ["string"]
        }}
      ]
    }}
  ],
  "level_differentiators": ["string"],
  "expected_scope": "string",
  "expected_impact": "string"
}}
'''
    # message = HumanMessage(content=prompt)
    print("state: ", state)
    txt_file = state["company_leveling_document"]
    with open(txt_file, 'r', encoding='utf-8') as file:
        content = file.read()
    query_engine = basic_example_gemini(document=content)
    competency_analyzer_output = query_engine.query(prompt)
    # response = llm.invoke([message])
    # famous_foods = [food.strip().replace('*', '').strip() for food in str(response.content).split('\n') if food.strip()]
    
    # Agent - Body part 

    # Task - Only 1 

    # handoff to gap analyzer 

    return {"competency_analyzer_output": competency_analyzer_output}
