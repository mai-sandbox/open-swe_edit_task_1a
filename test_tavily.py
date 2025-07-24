#!/usr/bin/env python3
"""Test script to investigate TavilySearch API parameters."""

import os
os.environ["TAVILY_API_KEY"] = "test_key"  # Set dummy key to avoid initialization errors

try:
    from langchain_tavily import TavilySearch
    import inspect
    
    # Try to create TavilySearch with search_depth parameter
    print("Testing TavilySearch parameters...")
    
    # Test 1: Basic initialization
    try:
        tavily_basic = TavilySearch(max_results=3)
        print("✅ Basic TavilySearch initialization successful")
    except Exception as e:
        print(f"❌ Basic initialization failed: {e}")
    
    # Test 2: With search_depth parameter
    try:
        tavily_advanced = TavilySearch(max_results=3, search_depth='advanced')
        print("✅ TavilySearch with search_depth='advanced' successful")
    except Exception as e:
        print(f"❌ TavilySearch with search_depth failed: {e}")
    
    # Test 3: Check available attributes/methods
    print("
    for attr in dir(TavilySearch):
        if not attr.startswith('_'):
            print(f"  {attr}")
except Exception as e:
    print(f"Error importing or testing TavilySearch: {e}")

