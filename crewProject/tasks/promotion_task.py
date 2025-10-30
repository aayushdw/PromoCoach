"""Promotion Package Builder Task"""
from crewai import Task
from agents.promotion_agent import create_promotion_agent


def create_promotion_task(state) -> Task:
    """Create promotion package builder task"""
    agent = create_promotion_agent()
    
    prompt = f"""Create a promotion package for {state.name} from {state.current_level} to {state.target_level[0] if state.target_level else 'target level'}.

CONTEXT:
- Engineer: {state.name}
- Current Level: {state.current_level}
- Target Level: {state.target_level}
- Discipline: {state.discipline}

EVIDENCE SOURCES:
- Project Contributions: {state.project_contributions[:1000] if state.project_contributions else 'Not provided'}
- Manager Notes: {state.manager_notes[:500] if state.manager_notes else 'Not provided'}
- Performance Reviews: {state.performance_reviews[:1000] if state.performance_reviews else 'Not provided'}
- Peer Feedback: {state.peer_feedback[:500] if state.peer_feedback else 'Not provided'}
- Self Assessment: {state.self_assessment[:500] if state.self_assessment else 'Not provided'}

COMPETENCY REQUIREMENTS:
{state.competency_analyzer_output[:1000] if state.competency_analyzer_output else 'Not yet available'}

YOUR TASK:
1. Create executive summary highlighting key achievements
2. Document specific accomplishments with evidence
3. Map contributions to target-level competencies
4. Include stakeholder feedback
5. Identify growth areas and recommendations

OUTPUT FORMAT:
Professional promotion package with:
- Executive summary
- Key accomplishments
- Competency evidence
- Project contributions
- Stakeholder feedback
- Growth areas
- Recommendations

Use professional, impactful language. Be honest and evidence-based. Never exaggerate."""

    return Task(
        description=prompt,
        agent=agent,
        expected_output="Professional promotion package document in markdown format"
    )

