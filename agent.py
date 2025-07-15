"""
React Agent Implementation

A LangGraph-based React agent for handling user queries with conversation memory.
"""

import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

# Load environment variables
load_dotenv()

def create_agent():
    """
    Creates a React agent for handling user queries.
    
    Returns:
        A configured LangGraph React agent with memory capabilities.
    """
    
    # Initialize the language model
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Configure Tavily search tool with advanced search depth
    tavily_tool = TavilySearch(
        max_results=3,
        api_key=os.getenv("TAVILY_API_KEY")
    )
    
    # Available tools for the agent
    tools = [tavily_tool]
    
    # Create memory checkpointer for conversation persistence
    checkpointer = InMemorySaver()
    
    # Create the React agent
    agent = create_react_agent(
        model=model,
        tools=tools,
        checkpointer=checkpointer
    )
    
    return agent

compiled_graph = create_agent()

