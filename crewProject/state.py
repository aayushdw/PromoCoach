"""
State management for CrewAI flow
Mirrors the GraphState from LangGraph version
"""
from typing import TypedDict, List, Optional
from pydantic import BaseModel


class WorkflowState(BaseModel):
    """State for the entire workflow"""
    # Core user information
    name: str = ""
    current_level: str = ""
    target_level: List[str] = []
    discipline: str = ""
    docs_updated: bool = False
    
    # Input documents and data
    company_leveling_document: str = ""
    manager_notes: str = ""
    performance_reviews: str = ""
    peer_feedback: str = ""
    self_assessment: str = ""
    project_contributions: str = ""
    
    # Opportunity context
    project_pipeline: str = ""
    company_initiatives: str = ""
    team_roadmap: str = ""
    learning_budget: str = ""
    workload_assessment: str = ""
    learning_style: str = ""
    time_availability: str = ""
    interest_area: str = ""
    
    # Agent outputs
    competency_analyzer_output: str = ""
    gap_analyzer_output: str = ""
    opportunity_finder_output: str = ""
    progress_tracker_output: str = ""
    promotion_package_output: str = ""

