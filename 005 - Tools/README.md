# 5 - Tools

This agent demonstrates how to create and use custom tools. A `get_words` tool is defined to count the words in a text, and a `check_agent` uses this tool to validate the length of an article created by a `writer_agent`.

## Code

```python
from google.adk.agents import LoopAgent, LlmAgent
from google.adk.tools import ToolContext


def exit_loop(tool_context: ToolContext):
    """Call this function ONLY when the critique indicates no further changes are needed, signaling the iterative process should end."""
    print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    # Return empty dict as tools should typically return JSON-serializable output
    return {}


def get_words(text_input: str):
    """Returns the number of words in a text."""
    return {"word_count": len(text_input.split(" "))}


writer_agent = LlmAgent(
    name="writer_agent",
    instruction="Create an article about Google Cloud.",
    model="gemini-2.5-flash",
)

check_agent = LlmAgent(
    name="check_agent",
    instruction="Check if the generated article is approx. 100 words long by calling `get_words`. If it is, executed `exit_loop` otherwise guide the agent to rewrite with approx 100 words.",
    model="gemini-2.5-flash",
    tools=[get_words, exit_loop],
)

root_agent = LoopAgent(
    name="root_agent",
    sub_agents=[writer_agent, check_agent],
    max_iterations=10,
)
```
