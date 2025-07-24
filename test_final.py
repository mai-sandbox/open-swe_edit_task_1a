import os
os.environ['OPENAI_API_KEY'] = 'test'
os.environ['TAVILY_API_KEY'] = 'test'
from agent import compiled_graph
print('SUCCESS: Agent imports correctly')
