from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool, FunctionTool


def get_words(text_input: str):
    """Returns the number of words in a text."""
    return {'word_count': len(text_input.split(' '))}


check_agent = LlmAgent(
    name='check_agent',
    instruction='Call `get_words` to check if the generated article is approx. 100 words long.',
    model='gemini-2.5-flash',
    tools=[FunctionTool(get_words)],
)

root_agent = LlmAgent(
    name='root_agent',
    instruction='Create an article about Google Cloud that has 100 words. Use check_agent to verify the number of words.',
    model='gemini-2.5-flash',
    tools=[AgentTool(agent=check_agent)],
)
