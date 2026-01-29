"""
Base Agent Template
This provides a foundational structure for building reasoning agents.
Extend this class to create specialized agents for your multi-agent system.
"""

import os
from abc import ABC, abstractmethod
from typing import Any
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


class BaseAgent(ABC):
    """
    Abstract base class for all agents in the multi-agent system.
    
    Extend this class to create specialized agents like:
    - LearningPathCurator
    - StudyPlanGenerator
    - EngagementAgent
    - AssessmentAgent
    
    Example:
        class LearningPathCurator(BaseAgent):
            def __init__(self):
                super().__init__(
                    name="Learning Path Curator",
                    role="Suggests relevant Microsoft Learn paths based on topics"
                )
            
            async def process(self, input_data):
                # Your agent logic here
                return curated_paths
    """
    
    def __init__(self, name: str, role: str):
        """
        Initialize the agent.
        
        Args:
            name: Human-readable name for the agent
            role: Description of what this agent does
        """
        self.name = name
        self.role = role
        
        # Load Azure AI Foundry settings
        self.connection_string = os.getenv("AZURE_AI_PROJECT_CONNECTION_STRING")
        self.model_deployment = os.getenv("AZURE_AI_MODEL_DEPLOYMENT", "gpt-4o")
        
    def __repr__(self) -> str:
        return f"Agent(name='{self.name}', role='{self.role}')"
    
    def get_ai_client(self):
        """
        Get an Azure AI Projects client.
        
        Returns:
            AIProjectClient configured with your credentials
        """
        from azure.ai.projects import AIProjectClient
        from azure.identity import DefaultAzureCredential
        
        if self.connection_string:
            return AIProjectClient.from_connection_string(
                credential=DefaultAzureCredential(),
                conn_str=self.connection_string
            )
        else:
            raise ValueError(
                "AZURE_AI_PROJECT_CONNECTION_STRING not set. "
                "Get it from ai.azure.com → Project settings → Project properties"
            )
    
    @abstractmethod
    async def process(self, input_data: dict[str, Any]) -> dict[str, Any]:
        """
        Process input and return output.
        
        This is the main method where agent logic is implemented.
        Override this method in your specialized agents.
        
        Args:
            input_data: Dictionary containing input for this agent
            
        Returns:
            Dictionary containing the agent's output
        """
        pass
    
    async def validate_input(self, input_data: dict[str, Any]) -> bool:
        """
        Validate input data before processing.
        Override this method to add custom validation logic.
        """
        return input_data is not None
    
    async def run(self, input_data: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the agent: validate -> process.
        
        Args:
            input_data: Input for the agent
            
        Returns:
            Processed output from the agent
        """
        if not await self.validate_input(input_data):
            raise ValueError(f"Invalid input for agent '{self.name}'")
        
        return await self.process(input_data)
