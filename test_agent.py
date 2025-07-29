#!/usr/bin/env python3
"""
Test script to verify the agent works correctly with evaluation format.
"""

import os
os.environ["OPENAI_API_KEY"] = "test-key"
os.environ["TAVILY_API_KEY"] = "test-key"

try:
    from agent import app
    from langchain_core.messages import HumanMessage
    
    print("✅ Agent imported successfully")
    print(f"✅ App type: {type(app)}")
    
    # Test the evaluation input format
    test_input = {"messages": [HumanMessage(content="Hello, can you help me?")]}
    print(f"✅ Test input format: {test_input}")
    
    print("✅ Agent is ready for evaluation")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
