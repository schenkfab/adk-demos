# 1 - LlmAgent

This agent demonstrates the fundamental `LlmAgent`. It shows how to define an agent with a name, description, model, and instruction. It also covers adding a `static_instruction` for context caching and defining an `output_schema` for structured output.

## Code

```python
from google.adk.agents import LlmAgent
from google.genai import types
from pydantic import BaseModel


# Defining an Agent with minimal information

root_agent = LlmAgent(
    # BaseAgent Parameters
    name="greeting_agent",
    description="An agent that greets the user in a random language.",
    # LlmAgent Parameters
    model="gemini-2.5-flash",
    instruction="Greet the user nicely in a random language.",
)

# Adding static_instructions to optimize context caching

root_agent = LlmAgent(
    # BaseAgent Parameters
    name="greeting_agent",
    description="An agent that greets the user in a random language.",
    # LlmAgent Parameters
    model="gemini-2.5-flash",
    instruction="Greet the user nicely in a random language.",
    static_instruction=types.Content(
        role="user",
        parts=[
            types.Part(text="You are a helpful assistant."),
        ],
    ),
)

# Adding an output_schema


class TranslatedContent(BaseModel):
    content: str
    language: str


root_agent = LlmAgent(
    # BaseAgent Parameters
    name="greeting_agent",
    description="An agent that greets the user in a random language.",
    # LlmAgent Parameters
    model="gemini-2.5-flash",
    instruction="Greet the user nicely in a random language.",
    static_instruction=types.Content(
        role="user",
        parts=[
            types.Part(text="You are a helpful assistant."),
        ],
    ),
    output_schema=TranslatedContent,
)
```
