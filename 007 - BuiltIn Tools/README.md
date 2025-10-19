# 7 - BuiltIn Tools

This agent shows how to use the built-in `google_search` tool. The agent is configured to act as a search specialist, demonstrating how to integrate pre-built functionalities.

## Code

```python
from google.adk.tools import google_search
from google.adk import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="""
    You're a specialist in Google Search.
    """,
    tools=[google_search],
)
```
