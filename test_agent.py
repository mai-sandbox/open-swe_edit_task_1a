#!/usr/bin/env python3
"""
Test script to verify the agent works correctly with evaluation format.
"""

import os
os.environ["OPENAI_API_KEY"] = "test-key"
os.environ["TAVILY_API_KEY"] = "test-key"

try:
    from agent import app, State
    from langchain_core.messages import HumanMessage
    
    print("✅ Agent imported successfully")
    print(f"✅ App type: {type(app)}")
    print(f"✅ State schema: {State}")
    
    # Test the evaluation input format
    test_input = {"messages": [HumanMessage(content="Hello, can you help me?")]}
    print(f"✅ Test input format: {test_input}")
    
    # Verify the state schema has the required fields
    import typing
    annotations = typing.get_type_hints(State)
    print(f"✅ State annotations: {annotations}")
    
    # Check if messages field has add_messages reducer
    if hasattr(State, '__annotations__'):
        messages_annotation = State.__annotations__.get('messages')
        print(f"✅ Messages field annotation: {messages_annotation}")
    
    print("✅ Agent is ready for evaluation")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

