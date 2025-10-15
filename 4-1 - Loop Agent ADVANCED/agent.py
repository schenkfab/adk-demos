from google.adk.agents import LoopAgent, LlmAgent
from google.adk.tools import ToolContext


first_agent = LlmAgent(
    name='german_agent',
    description='An agent that greets the user in german.',
    model='gemini-2.5-flash-lite',
    instruction='Greet the user nicely in German',
)

root_agent = LoopAgent(name='root_agent', sub_agents=[first_agent], max_iterations=3)


# Advanced Example


def exit_loop(tool_context: ToolContext):
    """Call this function ONLY when the critique indicates no further changes are needed, signaling the iterative process should end."""
    print(f'  [Tool Call] exit_loop triggered by {tool_context.agent_name}')
    tool_context.actions.escalate = True
    # Return empty dict as tools should typically return JSON-serializable output
    return {}


writer_agent = LlmAgent(
    name='writer_agent',
    instruction='Create an article about Google Cloud.',
    model='gemini-2.5-flash',
)

check_agent = LlmAgent(
    name='check_agent',
    instruction='Check if the generated article is approx. 100 words long. If it is, executed `exit_loop` otherwise guide the agent to rewrite with approx 100 words.',
    model='gemini-2.5-flash',
    tools=[exit_loop],
)

root_agent = LoopAgent(
    name='root_agent',
    sub_agents=[writer_agent, check_agent],
    max_iterations=3,
)
