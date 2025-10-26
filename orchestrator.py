from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END, START
from langgraph.types import Send
from typing import TypedDict, cast, List, Dict, Annotated
from llm_provider import get_llm
import operator
from agents import competency_analyzer


#file -> state 
class GraphState(TypedDict):
    name: str
    current_level: str
    target_level: List[str]
    company_leveling_document: str
    competency_analyzer_output: str

# maintain diff. state for each agent 
class CompetencyAnalyzerState(TypedDict):
    company_leveling_document: str

class GapAnalyzerState(TypedDict):
    manager_notes: str
    performance_reviews: str
    peer_feedback: str
    self_assessment: str
    project_contributions: str

class OpportunityFinder(TypedDict):
    project_pipeline: str
    company_initiatives: str
    team_roadmap: str
    learning_budget: str
    workload_assessment: str
    learning_style: str
    time_availability: str
    interest_area: str

def workflow_execution(args):
    workflow = StateGraph(GraphState)
    workflow.add_node("competency_analyzer", competency_analyzer.competency_analyzer_execute)
    
    workflow.add_edge(START, "competency_analyzer")
    workflow.add_edge("competency_analyzer", END)

    app = workflow.compile()

    final_state = app.invoke(cast(GraphState, {"name": args.name, "current_level": args.current_level, "target_level": args.target_level, "company_leveling_document": args.company_leveling_document}))
    
    return final_state["competency_analyzer_output"]
