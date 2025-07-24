import os
os.environ['OPENAI_API_KEY'] = 'test_key'
os.environ['TAVILY_API_KEY'] = 'test_key'

try:
    from langgraph.graph.graph import CompiledGraph
    print('✅ CompiledGraph from langgraph.graph.graph import successful')
except Exception as e:
    print(f'❌ CompiledGraph from langgraph.graph.graph import failed: {e}')
    
try:
    from langgraph.graph import CompiledGraph
    print('✅ CompiledGraph from langgraph.graph import successful')
except Exception as e:
    print(f'❌ CompiledGraph from langgraph.graph import failed: {e}')
    
try:
    from langgraph import CompiledGraph
    print('✅ CompiledGraph from langgraph import successful')
except Exception as e:
    print(f'❌ CompiledGraph from langgraph import failed: {e}')
