from google.adk.agents import LoopAgent, LlmAgent


first_agent = LlmAgent(
    name="german_agent",
    description="An agent that greets the user in german.",
    model="gemini-2.5-flash-lite",
    instruction="Greet the user nicely in German",
)

root_agent = LoopAgent(name="root_agent", sub_agents=[first_agent], max_iterations=3)
