"""
React Agent Implementation

A LangGraph-based React agent for handling user queries with conversation memory.
"""

import os
from dotenv import load_dotenv
from typing import List, Optional
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.graph.graph import CompiledGraph
from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

# Load environment variables
load_dotenv()

def create_agent():
    """Creates a React agent for handling user queries with web search capabilities.
    Creates a React agent for handling user queries.
    
    Returns:
        A configured LangGraph React agent with memory capabilities.
    """
    
    # Initialize the language model
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is required. "
            "Please set it in your .env file or environment."
        )
    
    tavily_api_key: Optional[str] = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError(
            "TAVILY_API_KEY environment variable is required. "
            "Please set it in your .env file or environment."
        )
    
    try:
        model: ChatOpenAI = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            api_key=openai_api_key
        )
    except Exception as e:
        raise RuntimeError(f"Failed to initialize ChatOpenAI model: {e}")
    
    # Initialize Tavily search tool
    try:
        tavily_search: TavilySearch = TavilySearch(
            max_results=3,
            search_depth="advanced"
        )
    except Exception as e:
        raise RuntimeError(f"Failed to initialize TavilySearch tool: {e}")
    
    tools: List[BaseTool] = [tavily_search]
    
    # Create memory checkpointer for conversation persistence
    checkpointer: BaseCheckpointSaver = InMemorySaver()
    
    # Create the React agent
    try:
        agent: CompiledGraph = create_react_agent(
            model=model,
            tools=tools,
            checkpointer=checkpointer
        )
    except Exception as e:
        raise RuntimeError(f"Failed to create React agent: {e}")
    
    return agent

# Initialize the compiled graph with proper error handling
try:
    compiled_graph: CompiledGraph = create_agent()
except Exception as e:
    raise RuntimeError(f"Failed to initialize agent: {e}")



