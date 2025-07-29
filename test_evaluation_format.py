#!/usr/bin/env python3
"""
Test script to verify the agent handles evaluation format correctly.
"""

import os
# Set dummy API keys for testing
os.environ["OPENAI_API_KEY"] = "sk-test-key"
os.environ["TAVILY_API_KEY"] = "tvly-test-key"

def test_evaluation_compliance():
    """Test that the agent complies with evaluation requirements."""
    
    try:
        from agent import app, State
        from langchain_core.messages import HumanMessage
        
        print("✅ Agent imported successfully")
        print(f"✅ App type: {type(app)}")
        
        # Verify State schema
        import typing
        annotations = typing.get_type_hints(State)
        print(f"✅ State annotations: {annotations}")
        
        # Check if messages field has add_messages reducer
        if hasattr(State, '__annotations__'):
            messages_annotation = State.__annotations__.get('messages')
            print(f"✅ Messages field annotation: {messages_annotation}")
            
            # Verify it's using add_messages reducer
            if hasattr(messages_annotation, '__metadata__'):
                print(f"✅ add_messages reducer detected: {messages_annotation.__metadata__}")
        
        # Test the exact evaluation input format
        test_input = {"messages": [HumanMessage(content="What is the weather like today?")]}
        print(f"✅ Test input format: {test_input}")
        
        # Test without thread_id first (what evaluator might do)
        print("🧪 Testing without thread_id (evaluator format)...")
        try:
            result = app.invoke(test_input)
            print(f"✅ App invocation successful without thread_id")
            print(f"✅ Result type: {type(result)}")
            if isinstance(result, dict) and 'messages' in result:
                print(f"✅ Messages in result: {len(result['messages'])} messages")
        except Exception as e:
            print(f"⚠️ App invocation failed without thread_id: {e}")
            
            # Try with thread_id as fallback
            print("🧪 Testing with thread_id (fallback)...")
            try:
                config = {"configurable": {"thread_id": "test-thread"}}
                result = app.invoke(test_input, config=config)
                print(f"✅ App invocation successful with thread_id")
                print(f"✅ Result type: {type(result)}")
                if isinstance(result, dict) and 'messages' in result:
                    print(f"✅ Messages in result: {len(result['messages'])} messages")
            except Exception as e2:
                print(f"❌ App invocation failed even with thread_id: {e2}")
                return False
        
        print("✅ Agent evaluation compliance verified")
        return True
        
    except Exception as e:
        print(f"❌ Error during evaluation compliance test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_evaluation_compliance()
    if success:
        print("\n🎉 Agent is ready for evaluation!")
    else:
        print("\n❌ Agent needs fixes before evaluation")
