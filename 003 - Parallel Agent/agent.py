from google.adk.agents import ParallelAgent, LlmAgent


first_agent = LlmAgent(
    name="german_agent",
    description="An agent that greets the user in german.",
    model="gemini-2.5-flash-lite",
    instruction="Greet the user nicely in German",
)

second_agent = LlmAgent(
    name="french_agent",
    description="An agent that greets the user in french.",
    model="gemini-2.5-flash-lite",
    instruction="Greet the user nicely in French",
)

third_agent = LlmAgent(
    name="spanish_agent",
    description="An agent that greets the user in spanish.",
    model="gemini-2.5-flash-lite",
    instruction="Greet the user nicely in Spanish",
)

# The parallel agent will execute all three agents in parallel without 
# waiting for any of them to finish.

root_agent = ParallelAgent(
    name="root_agent", sub_agents=[first_agent, second_agent, third_agent]
)
