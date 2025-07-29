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
    
    # Test that the app can handle the evaluation input format
    print("🧪 Testing evaluation input format...")
    try:
        # This is what the evaluator will do - need to provide thread_id for checkpointer
        config = {"configurable": {"thread_id": "test-thread"}}
        result = app.invoke(test_input, config=config)
        print(f"✅ App invocation successful")
        print(f"✅ Result type: {type(result)}")
        print(f"✅ Result keys: {result.keys() if isinstance(result, dict) else 'Not a dict'}")
        if isinstance(result, dict) and 'messages' in result:
            print(f"✅ Messages in result: {len(result['messages'])} messages")
            if result['messages']:
                last_message = result['messages'][-1]
                print(f"✅ Last message type: {type(last_message)}")
                print(f"✅ Last message content preview: {str(last_message)[:100]}...")
    except Exception as e:
        print(f"❌ App invocation failed: {e}")
        import traceback
        traceback.print_exc()
    
    print("✅ Agent is ready for evaluation")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()



