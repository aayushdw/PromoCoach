import argparse
import os
import re
from dotenv import load_dotenv
import orchestrator

# Load the .env file from the project root
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

if __name__ == "__main__":
    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found in .env file.")
    else:
        #  I/P and O/P execution 
        parser = argparse.ArgumentParser(description="Explore cuisines for a given location.")
        parser.add_argument("name", type=str, help="Name")
        parser.add_argument("current_level", type=str, help="Current Level")
        parser.add_argument("target_level", type=str, help="Target Level")
        parser.add_argument("company_leveling_document", type=str, help="company_leveling_document")

        args = parser.parse_args()


        final_output = orchestrator.workflow_execution(args)

        print(final_output)