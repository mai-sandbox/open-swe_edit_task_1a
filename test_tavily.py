from langchain_tavily import TavilySearch
import inspect

# Check TavilySearch constructor signature
sig = inspect.signature(TavilySearch.__init__)
print(f"TavilySearch.__init__ signature: {sig}")

