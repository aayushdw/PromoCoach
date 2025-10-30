"""Promotion Package Builder Agent for CrewAI"""
from crewai import Agent
from llm_provider import get_llm


def create_promotion_agent() -> Agent:
    """Create the Promotion Package Builder Agent"""
    return Agent(
        role="Promotion Package Writer",
        goal="Create honest, professional, and impactful promotion packages that accurately represent an engineer's achievements",
        backstory="""You are an expert at crafting promotion packages that highlight engineers' 
        accomplishments in a compelling way. You use evidence-based writing, professional tone, 
        and impactful language. You ensure all claims are backed by actual data and never 
        exaggerate achievements.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

