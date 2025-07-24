#!/usr/bin/env python3
"""Test script to investigate TavilySearch API parameters."""

try:
    from langchain_tavily import TavilySearch
    import inspect
    
    # Get the signature of TavilySearch.__init__
    sig = inspect.signature(TavilySearch.__init__)
    print("TavilySearch.__init__ parameters:")
    for param_name, param in sig.parameters.items():
        if param_name != 'self':
            print(f"  {param_name}: {param}")
except Exception as e:
    print(f"Error: {e}")
