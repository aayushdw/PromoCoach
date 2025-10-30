"""CrewAI Flow for PromoCoach Workflow"""
from crewai import Crew, Process
from typing import Dict

from state import WorkflowState
from tasks.competency_task import create_competency_task
from tasks.gap_task import create_gap_task
from tasks.opportunity_task import create_opportunity_task
from tasks.promotion_task import create_promotion_task
from utils import save_md_output, load_txt_files, load_basic_info, save_basic_info
import os


def run_workflow():
    """Run the complete workflow using CrewAI"""
    # Initialize state
    state = WorkflowState()
    
    # Load inputs
    print("📋 Progress Tracker: Starting...")
    test_mode = os.getenv("TEST_MODE", "false").lower() == "true"
    basic_info = load_basic_info()
    
    if test_mode:
        if basic_info:
            state.name = basic_info.get("name", "")
            state.current_level = basic_info.get("current_level", "")
            state.target_level = [basic_info.get("target_level", "")]
            state.discipline = basic_info.get("discipline", "")
        else:
            state.name = "Test Engineer"
            state.current_level = "L4"
            state.target_level = ["L5"]
            state.discipline = "Software Engineering"
    else:
        docs_updated = input("\n🤔 Updated docs? (yes/no): ").strip().lower() == 'yes'
        state.docs_updated = docs_updated
        
        if docs_updated and basic_info:
            state.name = basic_info.get("name", "")
            state.current_level = basic_info.get("current_level", "")
            state.target_level = [basic_info.get("target_level", "")]
            state.discipline = basic_info.get("discipline", "")
        else:
            state.name = input("👤 Name: ").strip()
            state.current_level = input("📊 Current Level: ").strip()
            state.target_level = [input("🎯 Target Level: ").strip()]
            state.discipline = input("🔧 Discipline: ").strip()
            save_basic_info(state.name, state.current_level, 
                          state.target_level[0], state.discipline)
    
    # Load all text files
    txt_data = load_txt_files('data/')
    for key, value in txt_data.items():
        setattr(state, key, value)
    
    print(f"✅ Loaded data for {state.name}")
    
    # Step 1: Competency Analysis (if not skipped)
    if not state.docs_updated:
        print("\n🔍 Running Competency Analyzer...")
        competency_task = create_competency_task(state)
        competency_crew = Crew(
            agents=[competency_task.agent],
            tasks=[competency_task],
            process=Process.sequential,
            verbose=True
        )
        competency_result = competency_crew.kickoff()
        state.competency_analyzer_output = str(competency_result)
        save_md_output("competency_analyzer", str(competency_result), {
            "engineer_name": state.name,
            "current_level": state.current_level,
            "target_level": state.target_level[0] if state.target_level else "",
            "discipline": state.discipline
        })
    
    # Step 2: Gap Analysis and Promotion Package
    print("\n🔍 Running Gap Analyzer...")
    gap_task = create_gap_task(state)
    gap_crew = Crew(
        agents=[gap_task.agent],
        tasks=[gap_task],
        process=Process.sequential,
        verbose=True
    )
    gap_result = gap_crew.kickoff()
    state.gap_analyzer_output = str(gap_result)
    save_md_output("gap_analyzer", str(gap_result), {
        "engineer_name": state.name,
        "current_level": state.current_level,
        "target_level": state.target_level[0] if state.target_level else ""
    })
    
    print("\n📦 Running Promotion Package Builder...")
    promotion_task = create_promotion_task(state)
    promotion_crew = Crew(
        agents=[promotion_task.agent],
        tasks=[promotion_task],
        process=Process.sequential,
        verbose=True
    )
    promotion_result = promotion_crew.kickoff()
    state.promotion_package_output = str(promotion_result)
    save_md_output("promotion_package_builder", str(promotion_result), {
        "engineer_name": state.name,
        "current_level": state.current_level,
        "target_level": state.target_level[0] if state.target_level else ""
    })
    
    # Step 3: Opportunity Finder (after gap analysis)
    print("\n🎯 Running Opportunity Finder...")
    opportunity_task = create_opportunity_task(state)
    opportunity_crew = Crew(
        agents=[opportunity_task.agent],
        tasks=[opportunity_task],
        process=Process.sequential,
        verbose=True
    )
    opportunity_result = opportunity_crew.kickoff()
    state.opportunity_finder_output = str(opportunity_result)
    save_md_output("opportunity_finder", str(opportunity_result), {
        "engineer_name": state.name
    })
    
    return {
        "competency_analysis": state.competency_analyzer_output,
        "gap_analysis": state.gap_analyzer_output,
        "opportunities": state.opportunity_finder_output,
        "promotion_package": state.promotion_package_output
    }
