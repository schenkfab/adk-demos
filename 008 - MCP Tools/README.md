# 8 - MCP Tools

This example demonstrates the use of MCP (Multiple-Context Prompting) tools. The agent connects to an external MCP server using an `MCPToolset` to generate a custom greeting, showcasing how to extend agent capabilities with external services.

## Code

```python
from google.adk import Agent
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams, MCPToolset


root_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="""
    You are a specialist. Use the MCP Server to create a custom greeting.
    """,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://mcp-server-475207959809.us-central1.run.app/mcp"
            ),
        )
    ],
)
```
