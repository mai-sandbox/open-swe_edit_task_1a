import os
os.environ['OPENAI_API_KEY'] = 'test_key'
os.environ['TAVILY_API_KEY'] = 'test_key'

try:
    from langgraph.graph import CompiledGraph
    print('✅ CompiledGraph import successful')
except Exception as e:
    print(f'❌ CompiledGraph import failed: {e}')
    
try:
    from langgraph.prebuilt import create_react_agent
    print('✅ create_react_agent import successful')
except Exception as e:
    print(f'❌ create_react_agent import failed: {e}')
    
try:
    from langchain_tavily import TavilySearch
    print('✅ TavilySearch import successful')
except Exception as e:
    print(f'❌ TavilySearch import failed: {e}')
