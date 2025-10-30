"""Gap Analysis Task"""
from crewai import Task
from agents.gap_agent import create_gap_agent


def create_gap_task(state) -> Task:
    """Create gap analysis task"""
    agent = create_gap_agent()
    
    prompt = f"""Identify gaps between {state.name}'s current capabilities and target level requirements.

CONTEXT:
- Engineer: {state.name}
- Current Level: {state.current_level}
- Target Level: {state.target_level}
- Discipline: {state.discipline}

COMPETENCY REQUIREMENTS:
{state.competency_analyzer_output[:2000] if state.competency_analyzer_output else 'Not yet available'}

PERFORMANCE EVIDENCE:
- Manager Notes: {state.manager_notes[:500] if state.manager_notes else 'Not provided'}
- Performance Reviews: {state.performance_reviews[:500] if state.performance_reviews else 'Not provided'}
- Peer Feedback: {state.peer_feedback[:500] if state.peer_feedback else 'Not provided'}
- Self Assessment: {state.self_assessment[:500] if state.self_assessment else 'Not provided'}
- Project Contributions: {state.project_contributions[:500] if state.project_contributions else 'Not provided'}

YOUR TASK:
1. Compare current capabilities against target requirements
2. Identify specific gaps in skills, experience, and behaviors
3. Prioritize gaps based on impact and feasibility
4. Provide actionable recommendations

OUTPUT FORMAT:
Structured analysis with:
- Identified gaps
- Priority levels
- Evidence assessment
- Development recommendations"""

    return Task(
        description=prompt,
        agent=agent,
        expected_output="Structured gap analysis with prioritized development areas and recommendations"
    )

