"""
Example Agent Implementation
This demonstrates how to extend BaseAgent to create a specialized agent.
Use this as a template for building your own agents.
"""

from typing import Any
from .base_agent import BaseAgent


class LearningPathCuratorAgent(BaseAgent):
    """
    Example: Learning Path Curator Agent
    
    This agent suggests Microsoft Learn paths based on the topics
    a student wants to study for their certification exam.
    """
    
    def __init__(self):
        super().__init__(
            name="Learning Path Curator",
            role="Analyzes student topics and suggests relevant Microsoft Learn paths"
        )
        self.supported_certifications = [
            "AZ-900",  # Azure Fundamentals
            "AZ-104",  # Azure Administrator
            "AZ-204",  # Azure Developer
            "AI-900",  # AI Fundamentals
            "AI-102",  # AI Engineer
        ]
    
    async def validate_input(self, input_data: dict[str, Any]) -> bool:
        """Validate that required fields are present."""
        return "topics" in input_data
    
    async def process(self, input_data: dict[str, Any]) -> dict[str, Any]:
        """
        Process the student's topics and return suggested learning paths.
        
        In a real implementation, this would:
        1. Use the Azure AI client to call an LLM
        2. Query Microsoft Learn MCP server for relevant content
        3. Rank and filter the results
        """
        topics = input_data.get("topics", [])
        target_cert = input_data.get("certification", None)
        
        # TODO: Replace with actual Azure AI Foundry calls
        # Example of how to use the AI client:
        #
        # client = self.get_ai_client()
        # response = client.inference.chat_completions.create(
        #     model=self.model_deployment,
        #     messages=[
        #         {"role": "system", "content": "You are a learning path curator..."},
        #         {"role": "user", "content": f"Find learning paths for: {topics}"}
        #     ]
        # )
        
        # Placeholder response
        return {
            "agent": self.name,
            "input_topics": topics,
            "target_certification": target_cert,
            "learning_paths": [
                {
                    "title": "Example Learning Path",
                    "url": "https://learn.microsoft.com/...",
                    "duration_hours": 4,
                    "relevance_score": 0.95,
                },
            ],
            "next_steps": "Pass to Study Plan Generator agent",
        }


class StudyPlanGeneratorAgent(BaseAgent):
    """
    Example: Study Plan Generator Agent
    
    Takes curated learning paths and creates a structured study plan.
    """
    
    def __init__(self):
        super().__init__(
            name="Study Plan Generator",
            role="Creates structured study plans with timelines and milestones"
        )
    
    async def process(self, input_data: dict[str, Any]) -> dict[str, Any]:
        """Generate a study plan from learning paths."""
        learning_paths = input_data.get("learning_paths", [])
        
        # TODO: Implement with Azure AI Foundry
        return {
            "agent": self.name,
            "total_duration_weeks": 4,
            "weekly_hours": 10,
            "milestones": [
                {"week": 1, "goal": "Complete foundational modules"},
                {"week": 2, "goal": "Hands-on labs and exercises"},
                {"week": 3, "goal": "Practice assessments"},
                {"week": 4, "goal": "Final review and exam"},
            ],
        }


# Example usage
async def example_workflow():
    """Demonstrate how agents work together."""
    curator = LearningPathCuratorAgent()
    planner = StudyPlanGeneratorAgent()
    
    # Student input
    student_request = {
        "topics": ["Azure containers", "Kubernetes", "CI/CD"],
        "certification": "AZ-104",
    }
    
    # Agent 1: Curate learning paths
    paths = await curator.run(student_request)
    print(f"Curator: {paths}")
    
    # Agent 2: Generate study plan
    plan = await planner.run(paths)
    print(f"Plan: {plan}")
    
    return plan


if __name__ == "__main__":
    import asyncio
    asyncio.run(example_workflow())
