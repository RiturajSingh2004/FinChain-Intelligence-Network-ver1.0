"""
Base Agent Module - Defines the foundation for all specialized agents in the FinChain network.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
import logging


class BaseAgent(ABC):
    """
    Abstract base class for all FinChain Intelligence Network agents.
    Provides common functionality and interface that all agents must implement.
    """

    def __init__(self, name: str, description: str, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the base agent.
        
        Args:
            name: The name of the agent
            description: A brief description of the agent's capabilities
            config: Optional configuration parameters for the agent
        """
        self.name = name
        self.description = description
        self.config = config or {}
        self.logger = logging.getLogger(f"fin.agents.{name}")
        self._initialize_agent()
        
    def _initialize_agent(self):
        """Set up the agent with any necessary initializations."""
        self.logger.info(f"Initializing agent: {self.name}")
        
    @abstractmethod
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a user query and return results.
        
        Args:
            query: The user's query string
            
        Returns:
            A dictionary containing the agent's response
        """
        pass
    
    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """
        Return a list of the agent's capabilities.
        
        Returns:
            A list of capability descriptions
        """
        pass
    
    def health_check(self) -> Dict[str, Any]:
        """
        Verify the agent is functioning properly and all dependencies are available.
        
        Returns:
            A dictionary with health status information
        """
        return {
            "status": "healthy",
            "name": self.name,
            "version": self.__class__.__module__
        }
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}" 