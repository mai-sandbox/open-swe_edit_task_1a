import os
os.environ['OPENAI_API_KEY'] = 'test_key'
os.environ['TAVILY_API_KEY'] = 'test_key'

try:
    from agent import compiled_graph
    print('✅ Agent import successful')
    print(f'✅ compiled_graph type: {type(compiled_graph).__name__}')
except Exception as e:
    print(f'❌ Import failed: {e}')
