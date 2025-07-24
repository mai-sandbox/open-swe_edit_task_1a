"""
Final test to verify corrected imports and agent initialization
"""

import os

def test_imports():
    """Test that corrected imports work and agent initializes properly"""
    print("Testing corrected imports...")
    
    # Set dummy environment variables for testing
    os.environ["OPENAI_API_KEY"] = "test_key_for_import_verification"
    os.environ["TAVILY_API_KEY"] = "test_key_for_import_verification"
    
    try:
        # Test the corrected CompiledStateGraph import
        from langgraph.graph.state import CompiledStateGraph
        print("✅ CompiledStateGraph import successful")
        
        # Test agent module import
        from agent import compiled_graph, create_agent
        print("✅ Agent module imported successfully")
        
        # Verify compiled_graph type
        print(f"✅ compiled_graph type: {type(compiled_graph).__name__}")
        
        # Verify it's the correct type
        if isinstance(compiled_graph, CompiledStateGraph):
            print("✅ compiled_graph correctly typed as CompiledStateGraph")
            return True
        else:
            print(f"❌ Type mismatch: expected CompiledStateGraph, got {type(compiled_graph)}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
