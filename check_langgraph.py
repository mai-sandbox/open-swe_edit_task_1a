import langgraph
print('langgraph attributes:', dir(langgraph))

from langgraph.prebuilt import create_react_agent
print('create_react_agent type:', type(create_react_agent))

# Check what create_react_agent returns
import os
os.environ['OPENAI_API_KEY'] = 'test_key'
os.environ['TAVILY_API_KEY'] = 'test_key'

from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver

model = ChatOpenAI(model='gpt-4o-mini', temperature=0, api_key='test')
tools = [TavilySearch(max_results=3, search_depth='advanced')]
checkpointer = InMemorySaver()

agent = create_react_agent(model=model, tools=tools, checkpointer=checkpointer)
print('Agent type:', type(agent))
print('Agent attributes:', [attr for attr in dir(agent) if not attr.startswith('_')])
