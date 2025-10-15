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
