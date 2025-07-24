"""
Simple test for React Agent implementation
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    print("🚀 Testing React Agent Implementation")
    print("=" * 50)
    
    # Test 1: Environment variables
    print("\n1. Testing environment variables...")
    openai_key = os.getenv("OPENAI_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")
    
    if openai_key and tavily_key:
        print("✅ Environment variables configured")
    else:
        print("❌ Missing environment variables")
        return False
    
    # Test 2: Agent import
    print("\n2. Testing agent import...")
    try:
        from agent import compiled_graph
        print("✅ Agent imported successfully")
        print(f"✅ compiled_graph type: {type(compiled_graph)}")
    except Exception as e:
        print(f"❌ Failed to import agent: {e}")
        return False
    
    # Test 3: TavilySearch configuration
    print("\n3. Testing TavilySearch configuration...")
    try:
        from langchain_tavily import TavilySearch
        tavily_test = TavilySearch(max_results=3, search_depth="advanced")
        print("✅ TavilySearch configured with max_results=3 and search_depth='advanced'")
    except Exception as e:
        print(f"❌ TavilySearch configuration failed: {e}")
        return False
    
    print("\n🎉 ALL TESTS PASSED - Agent implementation is ready!")
    return True

if __name__ == "__main__":
    main()
