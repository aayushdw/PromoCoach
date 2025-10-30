"""Utility functions for file management"""
import os
import json
from typing import Dict, Optional
from datetime import datetime


def ensure_output_dir():
    """Create outputs/ directory if it doesn't exist."""
    if not os.path.exists("outputs"):
        os.makedirs("outputs")


def load_txt_files(directory: str = "data/") -> Dict[str, str]:
    """Load all .txt files from a directory."""
    txt_data = {}
    
    if not os.path.exists(directory):
        print(f"⚠️ Directory {directory} not found")
        return txt_data
    
    expected_files = {
        "company_leveling_document.txt": "company_leveling_document",
        "manager_notes.txt": "manager_notes",
        "performance_reviews.txt": "performance_reviews",
        "peer_feedback.txt": "peer_feedback",
        "self_assessment.txt": "self_assessment",
        "project_contributions.txt": "project_contributions",
        "project_pipeline.txt": "project_pipeline",
        "company_initiatives.txt": "company_initiatives",
        "team_roadmap.txt": "team_roadmap"
    }
    
    for filename, state_key in expected_files.items():
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    txt_data[state_key] = content
                    print(f"✅ Loaded {filename}")
            except Exception as e:
                print(f"⚠️ Error loading {filename}: {str(e)}")
    
    return txt_data


def save_md_output(agent_name: str, content: str, metadata: Optional[Dict] = None):
    """Save agent output to markdown file."""
    ensure_output_dir()
    filename = f"{agent_name}.md"
    filepath = os.path.join("outputs", filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            if metadata:
                f.write(f"# {agent_name.replace('_', ' ').title()}\n\n")
                for key, value in metadata.items():
                    f.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")
                f.write("---\n\n")
            f.write(content)
        print(f"✅ Saved output to {filepath}")
    except Exception as e:
        print(f"⚠️ Error saving output: {str(e)}")


def load_basic_info() -> Dict:
    """Load basic info from previous run."""
    filepath = "outputs/basic_info.json"
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_basic_info(name: str, current_level: str, target_level: str, discipline: str):
    """Save basic info for next run."""
    ensure_output_dir()
    filepath = "outputs/basic_info.json"
    data = {
        "name": name,
        "current_level": current_level,
        "target_level": target_level,
        "discipline": discipline,
        "timestamp": datetime.now().isoformat()
    }
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"⚠️ Error saving basic info: {str(e)}")

