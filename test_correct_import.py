import os
os.environ['OPENAI_API_KEY'] = 'test_key'
os.environ['TAVILY_API_KEY'] = 'test_key'

try:
    from langgraph.graph.state import CompiledStateGraph
    print('✅ CompiledStateGraph import successful')
    
    from langchain_openai import ChatOpenAI
    from langchain_tavily import TavilySearch
    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.prebuilt import create_react_agent
    
    model = ChatOpenAI(model='gpt-4o-mini', temperature=0, api_key='test')
    tools = [TavilySearch(max_results=3, search_depth='advanced')]
    checkpointer = InMemorySaver()
    
    agent = create_react_agent(model=model, tools=tools, checkpointer=checkpointer)
    print(f'✅ Agent created successfully, type: {type(agent)}')
    print(f'✅ Agent is instance of CompiledStateGraph: {isinstance(agent, CompiledStateGraph)}')
    
except Exception as e:
    print(f'❌ Error: {e}')
