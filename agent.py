# Required by ADK for proper Python type hints
from __future__ import annotations


from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

# Import the Agent class
from google.adk.agents import Agent

from google.adk.models.lite_llm import LiteLlm

# Define your agent - MUST be named 'root_agent'
root_agent = Agent(
    name="hello_assistant",
    model=LiteLlm (model = "ollama_chat/llama3.2"),
    description="A friendly AI assistant for general conversation",
    instruction=(
        "You are a warm and helpful assistant. "
        "Greet users enthusiastically and answer their questions clearly. "
        "Be conversational and friendly!"
    )
)