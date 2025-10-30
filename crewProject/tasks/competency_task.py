"""Competency Analysis Task"""
from crewai import Task
from agents.competency_agent import create_competency_agent


def create_competency_task(state) -> Task:
    """Create competency analysis task"""
    agent = create_competency_agent()
    
    prompt = f"""Analyze the competency requirements for promotion from {state.current_level} to {state.target_level[0] if state.target_level else 'target level'} in {state.discipline}.

CONTEXT:
- Engineer Name: {state.name}
- Current Level: {state.current_level}
- Target Level: {state.target_level}
- Discipline: {state.discipline}

COMPANY LEVELING DOCUMENT:
{state.company_leveling_document[:2000] if state.company_leveling_document else 'Not provided'}

YOUR TASK:
1. Parse and interpret the company leveling document
2. Identify technical, leadership, and soft skill requirements for the target level
3. Map discipline-specific expectations
4. Generate a comprehensive competency framework

OUTPUT FORMAT:
Provide a structured JSON response with:
- target_level
- current_level
- discipline
- competency_categories (with requirements, importance, evaluation_criteria)
- level_differentiators
- expected_scope
- expected_impact

Be professional, objective, and encouraging."""

    return Task(
        description=prompt,
        agent=agent,
        expected_output="Structured JSON analysis of competency requirements for target promotion level"
    )

