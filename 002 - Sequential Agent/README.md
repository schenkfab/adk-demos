# 2 - Sequential Agent

This example introduces the `SequentialAgent`, which executes a series of sub-agents in a predefined order. The included agent first greets the user and then says goodbye, showcasing a simple sequential workflow.

## Code

```python
from google.adk.agents import SequentialAgent, LlmAgent


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

root_agent = SequentialAgent(
    name="root_agent",
    sub_agents=[first_agent, second_agent] # The agents will run in the list order without LLM summarization from the root agent.
)
```
