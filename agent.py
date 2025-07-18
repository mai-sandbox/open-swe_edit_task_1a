"""
React Agent Implementation

A LangGraph-based React agent for handling user queries with conversation memory.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
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
    
    # Available tools for the agent
    tavily_search = TavilySearch(
        max_results=3,
        search_depth="advanced",
        api_key=os.getenv("TAVILY_API_KEY")
    )
    tools = [tavily_search]
    
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


