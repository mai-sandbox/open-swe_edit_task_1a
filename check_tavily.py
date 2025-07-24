import os
os.environ["TAVILY_API_KEY"] = "dummy_key"

try:
    from langchain_tavily import TavilySearch
    
    print("Testing TavilySearch parameters...")
    
    # Test basic initialization
    try:
        tavily_basic = TavilySearch(max_results=3)
        print("✅ Basic TavilySearch(max_results=3) works")
    except Exception as e:
        print(f"❌ Basic initialization failed: {e}")
    
    # Test with search_depth parameter
    try:
        tavily_advanced = TavilySearch(max_results=3, search_depth="advanced")
        print("✅ TavilySearch with search_depth='advanced' works")
    except Exception as e:
        print(f"❌ search_depth parameter failed: {e}")
        
except ImportError as e:
    print(f"Import error: {e}")

