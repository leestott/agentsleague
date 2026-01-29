"""
Main Entry Point for the Reasoning Agents Solution

This is the starting point for your multi-agent system.
Modify this file to build your certification exam preparation assistant.

Usage:
    python src/main.py
"""

import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


async def main():
    """
    Main entry point for the multi-agent system.
    
    TODO: Implement your multi-agent workflow here.
    
    Suggested steps:
    1. Parse student input (topics, target certification, timeline)
    2. Run the Learning Path Curator agent
    3. Run the Study Plan Generator agent  
    4. Run the Engagement agent (set up reminders)
    5. Wait for student confirmation
    6. Run the Assessment agent
    7. Based on results, schedule exam or loop back
    """
    print("🧠 Reasoning Agents - Certification Exam Prep Assistant")
    print("=" * 55)
    
    # Example student input
    student_input = {
        "topics": ["Azure fundamentals", "Cloud concepts", "Azure services"],
        "target_certification": "AZ-900",
        "study_weeks_available": 4,
        "hours_per_week": 10,
    }
    
    print(f"\n📚 Topics: {student_input['topics']}")
    print(f"🎯 Target: {student_input['target_certification']}")
    print(f"⏰ Time: {student_input['study_weeks_available']} weeks, "
          f"{student_input['hours_per_week']} hrs/week")
    
    # TODO: Add your agent orchestration logic here
    # See src/agents/example_agent.py for starter templates
    
    print("\n✨ Implement your multi-agent workflow in this file!")
    print("   Start with the agents in src/agents/")
    print("\n" + "=" * 55)


if __name__ == "__main__":
    asyncio.run(main())
