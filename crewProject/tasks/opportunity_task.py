"""Opportunity Finder Task"""
from crewai import Task
from agents.opportunity_agent import create_opportunity_agent


def create_opportunity_task(state) -> Task:
    """Create opportunity finder task"""
    agent = create_opportunity_agent()
    
    prompt = f"""Find growth opportunities for {state.name} to close identified gaps and advance their career.

CONTEXT:
- Engineer: {state.name}
- Gap Analysis: {state.gap_analyzer_output[:2000] if state.gap_analyzer_output else 'Not yet available'}
- Learning Budget: {state.learning_budget or '$2000'}
- Learning Style: {state.learning_style or 'Not specified'}
- Time Availability: {state.time_availability or 'Not specified'}

OPPORTUNITY SOURCES:
- Project Pipeline: {state.project_pipeline[:500] if state.project_pipeline else 'Not provided'}
- Company Initiatives: {state.company_initiatives[:500] if state.company_initiatives else 'Not provided'}
- Team Roadmap: {state.team_roadmap[:500] if state.team_roadmap else 'Not provided'}

YOUR TASK:
1. Plan which courses to search for based on gap analysis
2. Search for relevant learning courses online
3. Identify internal project opportunities
4. Match opportunities to specific gaps
5. Prioritize based on impact and feasibility

OUTPUT FORMAT:
Structured recommendations with:
- Learning courses (with links, prices, duration)
- Project opportunities
- Quick wins
- Stretch goals
- Recommended priorities"""

    return Task(
        description=prompt,
        agent=agent,
        expected_output="Comprehensive opportunity plan with courses and project recommendations"
    )

