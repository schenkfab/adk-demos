from google.adk.tools.application_integration_tool import ApplicationIntegrationToolset
from google.adk import Agent
import os

integration_tool = ApplicationIntegrationToolset(
        project=os.getenv("GOOGLE_CLOUD_PROJECT", "project"),
        location="us-central1", #TODO: replace with location of the connection
        integration="conversation_summary_cloudsql", #TODO: replace with integration name
        triggers=["api_trigger/_API_1"],#TODO: replace with trigger id(s). Empty list would mean all api triggers in the integration to be considered.
        tool_instructions="Usable to send an email of a conversation."
    )

root_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="""
    Use the `integration_tool` to send a summary of the conversation to the user once the user asks for it.
    """,
    tools=[integration_tool],
)
