"""Main entry point for CrewAI PromoCoach"""
import os
import sys
from dotenv import load_dotenv
from flows.workflow import run_workflow


def load_environment():
    """Load environment variables"""
    load_dotenv()
    
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY not found in .env file.")
        sys.exit(1)
    
    print("✅ Environment loaded successfully")


def main():
    """Main function"""
    print("🚀 PromoCoach - AI-Powered Career Development Assistant (CrewAI)")
    print("=" * 60)
    
    load_environment()
    
    print("\n🔄 Starting PromoCoach workflow...\n")
    
    try:
        results = run_workflow()
        
        print("\n" + "=" * 60)
        print("🎉 WORKFLOW COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print("\n📁 Output files saved in outputs/ directory:")
        print("  • competency_analyzer.md")
        print("  • gap_analyzer.md")
        print("  • opportunity_finder.md")
        print("  • promotion_package_builder.md")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

