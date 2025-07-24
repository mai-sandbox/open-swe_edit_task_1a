"""
Comprehensive verification of React Agent implementation
Tests all requirements: Tavily integration, memory, configuration
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_environment_setup():
    """Verify environment configuration is properly documented"""
    print("1. Testing environment setup...")
    
    if not os.path.exists(".env.example"):
        print("❌ .env.example file missing")
        return False
    
    with open(".env.example", "r") as f:
        content = f.read()
        
    if "OPENAI_API_KEY" in content and "TAVILY_API_KEY" in content:
        print("✅ Required environment variables documented in .env.example")
        return True
    else:
        print("❌ Missing required environment variables in .env.example")
        return False

def test_agent_import():
    """Test agent import with dummy environment variables"""
    print("\n2. Testing agent import...")
    
    # Set dummy environment variables for testing
    os.environ["OPENAI_API_KEY"] = "test_openai_key"
    os.environ["TAVILY_API_KEY"] = "test_tavily_key"
    
    try:
        from agent import compiled_graph, create_agent
        print("✅ Agent module imports successfully")
        print(f"✅ compiled_graph type: {type(compiled_graph)}")
        return True
    except Exception as e:
        print(f"❌ Failed to import agent: {e}")
        return False

def test_tavily_configuration():
    """Verify TavilySearch configuration supports our parameters"""
    print("\n3. Testing TavilySearch configuration...")
    
    try:
        from langchain_tavily import TavilySearch
        
        # Test our specific configuration
        tavily_test = TavilySearch(max_results=3, search_depth="advanced")
        print("✅ TavilySearch supports max_results=3")
        print("✅ TavilySearch supports search_depth='advanced'")
        return True
        
    except Exception as e:
        print(f"❌ TavilySearch configuration failed: {e}")
        return False

def test_agent_structure():
    """Verify agent.py contains all required components"""
    print("\n4. Testing agent structure...")
    
    try:
        with open("agent.py", "r") as f:
            content = f.read()
        
        checks = [
            ("create_react_agent", "Uses create_react_agent from langgraph.prebuilt"),
            ("InMemorySaver", "Uses InMemorySaver for conversation memory"),
            ("max_results=3", "TavilySearch configured with max_results=3"),
            ('search_depth="advanced"', "TavilySearch configured with search_depth='advanced'"),
            ("compiled_graph", "Exports compiled_graph for evaluation")
        ]
        
        for check, description in checks:
            if check in content:
                print(f"✅ {description}")
            else:
                print(f"❌ Missing: {description}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Agent structure verification failed: {e}")
        return False

def main():
    """Run all verification tests"""
