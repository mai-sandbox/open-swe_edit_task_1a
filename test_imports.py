"""
Test script to verify corrected imports and agent initialization
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_corrected_imports():
    """Test that the corrected imports work properly"""
    print("🔧 Testing corrected imports...")
    
    # Set dummy environment variables for testing
    os.environ["OPENAI_API_KEY"] = "test_openai_key_for_import_test"
    os.environ["TAVILY_API_KEY"] = "test_tavily_key_for_import_test"
    
    try:
        # Test the corrected import
        from langgraph.graph.state import CompiledStateGraph
        print("✅ CompiledStateGraph import successful")
        
        # Test agent module import
        from agent import compiled_graph, create_agent
        print("✅ Agent module imported successfully")
        
        # Verify compiled_graph type
        print(f"✅ compiled_graph type: {type(compiled_graph)}")
        
        # Verify it's the correct type
        if isinstance(compiled_graph, CompiledStateGraph):
            print("✅ compiled_graph is correctly typed as CompiledStateGraph")
        else:
            print(f"❌ compiled_graph type mismatch: expected CompiledStateGraph, got {type(compiled_graph)}")
            return False
            
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during import: {e}")
        return False

def main():
    """Run import tests"""
    print("🚀 Testing Corrected Imports and Agent Initialization")
    print("=" * 60)
    
    # Test corrected imports
    import_success = test_corrected_imports()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 IMPORT TEST SUMMARY")
    print("=" * 60)
    
    if import_success:
        print("🎉 ALL IMPORT TESTS PASSED!")
        print("✅ CompiledStateGraph import: SUCCESSFUL")
        print("✅ Agent module import: SUCCESSFUL") 
        print("✅ compiled_graph initialization: SUCCESSFUL")
