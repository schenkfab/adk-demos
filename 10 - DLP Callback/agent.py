from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_response import LlmResponse
from google.adk.models.llm_request import LlmRequest
from typing import Optional
from google.genai import types
from .dlp import identify


def check_before_model(
    callback_context: CallbackContext, llm_request: LlmRequest
) -> Optional[LlmResponse]:
    """Checks for sensitive data before calling the model.

    Args:
        callback_context: The callback context.
        llm_request: The LLM request.

    Returns:
        An LlmResponse if sensitive data is found, otherwise None.
    """
    # The relevant part is the last part from the user:
    relevant_part = [
        content.parts for content in llm_request.contents if content.role == "user"
    ][-1]
    if relevant_part and relevant_part[0].text:
        findings = identify(relevant_part[0].text)
        if findings.includes_finding:
            callback_context.session.events[-1].content = types.Content(
                parts=[types.Part(text="REDACTED")]
            )
            output_string = f"Found the following information: {str(findings)}"
            return LlmResponse(
                content=types.Content(
                    role="model",
                    parts=[types.Part(text=output_string)],
                )
            )


root_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="""
    Use the `integration_tool` to send a summary of the conversation to the user once the user asks for it.
    """,
    before_model_callback=check_before_model,
)
