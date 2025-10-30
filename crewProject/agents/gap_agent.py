"""Gap Analyzer Agent for CrewAI"""
from crewai import Agent
from llm_provider import get_llm


def create_gap_agent() -> Agent:
    """Create the Gap Analyzer Agent"""
    return Agent(
        role="Career Gap Analysis Specialist",
        goal="Identify gaps between an engineer's current capabilities and target promotion level requirements",
        backstory="""You are a career development expert who specializes in gap analysis. 
        You carefully compare engineers' current performance, skills, and achievements against 
        target-level requirements. You identify specific areas for development and prioritize 
        them based on impact and feasibility.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

