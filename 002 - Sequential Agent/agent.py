from google.adk.agents import LlmAgent, SequentialAgent

first_agent = LlmAgent(
    name="greeting_agent",
    description="An agent that greets the user in a random language.",
    model="gemini-2.5-flash-lite",
    instruction="Greet the user nicely in a random language.",
)

second_agent = LlmAgent(
    name="goodbye_agent",
    description="An agent that says good bye the user in a random language.",
    model="gemini-2.5-flash-lite",
    instruction="Use the same language as the last message and say good bye in the same language.",
)

# The root agent itself will not use an LLM and execute in the exact order
# as in the sub_agents list.

root_agent = SequentialAgent(name="root_agent", sub_agents=[first_agent, second_agent])
