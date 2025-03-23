"""
FinChain Orchestrator - Coordinates all specialized agents in the FinChain Intelligence Network.
"""

import logging
from typing import Dict, List, Any, Optional, Type
from .base_agent import BaseAgent


class FinChainOrchestrator:
    """
    The FinChain Orchestrator is responsible for:
    1. Managing all specialized agents in the network
    2. Routing user queries to the appropriate agents
    3. Synthesizing responses from multiple agents
    4. Providing a unified interface for users
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the FinChain Orchestrator.
        
        Args:
            config: Optional configuration parameters
        """
        self.logger = logging.getLogger("fin.orchestrator")
        self.config = config or {}
        self.agents = {}
        self._initialize_orchestrator()
        
    def _initialize_orchestrator(self):
        """Set up the orchestrator with default agents and configurations."""
        self.logger.info("Initializing FinChain Orchestrator")
        
    def register_agent(self, agent: BaseAgent):
        """
        Register a new agent with the orchestrator.
        
        Args:
            agent: The agent instance to register
        """
        self.agents[agent.name] = agent
        self.logger.info(f"Registered agent: {agent.name}")
        
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a user query by routing it to the appropriate agents and synthesizing responses.
        
        Args:
            query: The user's query string
            
        Returns:
            A dictionary containing the orchestrated response
        """
        self.logger.info(f"Processing query: {query}")
        
        # 1. Analyze the query to determine which agents should handle it
        relevant_agents = self._identify_relevant_agents(query)
        
        # 2. Route the query to the relevant agents and collect their responses
        agent_responses = {}
        for agent_name in relevant_agents:
            if agent_name in self.agents:
                agent_responses[agent_name] = self.agents[agent_name].process_query(query)
            
        # 3. Synthesize the responses into a coherent answer
        synthesized_response = self._synthesize_responses(query, agent_responses)
        
        return synthesized_response
    
    def _identify_relevant_agents(self, query: str) -> List[str]:
        """
        Determine which agents are most relevant for the given query.
        
        Args:
            query: The user's query string
            
        Returns:
            A list of agent names that should process the query
        """
        # In a real implementation, this would use NLP to match the query to agent capabilities
        # For now, we'll use a simplified approach
        relevant_agents = []
        
        # Check for blockchain related queries
        if any(term in query.lower() for term in ["blockchain", "transaction", "smart contract", "crypto"]):
            relevant_agents.append("blockchain_analyst")
            
        # Check for fintech related queries
        if any(term in query.lower() for term in ["fintech", "payment", "banking", "financial news"]):
            relevant_agents.append("fintech_navigator")
            
        # Check for ML/investment related queries
        if any(term in query.lower() for term in ["investment", "predict", "portfolio", "strategy"]):
            relevant_agents.append("ml_investment_strategist")
            
        # Check for crypto economics related queries
        if any(term in query.lower() for term in ["token", "defi", "yield", "tokenomics"]):
            relevant_agents.append("crypto_economics")
            
        # Check for regulatory related queries
        if any(term in query.lower() for term in ["regulation", "compliance", "legal", "jurisdiction"]):
            relevant_agents.append("regulatory_compliance")
            
        # If no specific agents were identified, use all agents
        if not relevant_agents:
            relevant_agents = list(self.agents.keys())
            
        return relevant_agents
    
    def _synthesize_responses(self, query: str, agent_responses: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Synthesize responses from multiple agents into a coherent answer.
        
        Args:
            query: The original user query
            agent_responses: Dictionary mapping agent names to their responses
            
        Returns:
            A unified response dictionary
        """
        # In a real implementation, this would use LLMs to synthesize responses
        # For now, we'll use a simplified approach
        
        synthesized = {
            "query": query,
            "agents_consulted": list(agent_responses.keys()),
            "insights": [],
            "recommendations": [],
            "confidence": 0.0
        }
        
        # Extract insights and recommendations from each agent response
        for agent_name, response in agent_responses.items():
            if "insights" in response:
                for insight in response["insights"]:
                    synthesized["insights"].append({
                        "content": insight,
                        "source": agent_name
                    })
                    
            if "recommendations" in response:
                for recommendation in response["recommendations"]:
                    synthesized["recommendations"].append({
                        "content": recommendation,
                        "source": agent_name
                    })
                    
            # Aggregate confidence scores
            if "confidence" in response:
                synthesized["confidence"] += response["confidence"] / len(agent_responses)
        
        return synthesized
    
    def get_registered_agents(self) -> List[str]:
        """
        Return a list of all registered agent names.
        
        Returns:
            A list of agent names
        """
        return list(self.agents.keys())
    
    def health_check(self) -> Dict[str, Any]:
        """
        Perform a health check on all registered agents.
        
        Returns:
            A dictionary with health status information for the orchestrator and all agents
        """
        results = {
            "orchestrator": {
                "status": "healthy",
                "agent_count": len(self.agents)
            },
            "agents": {}
        }
        
        for agent_name, agent in self.agents.items():
            results["agents"][agent_name] = agent.health_check()
            
        return results 