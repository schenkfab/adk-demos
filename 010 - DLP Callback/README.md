# DLP Callback Agent

This agent demonstrates how to use a `before_model_callback` to check for sensitive data using the Data Loss Prevention (DLP) API before sending the request to the model.

## How it works

The `check_before_model` function in `agent.py` is registered as a `before_model_callback`.
This function takes the `LlmRequest` and inspects the content for sensitive information using the `identify` function from `dlp.py`.

If sensitive data is found, the agent redacts the user's message, and instead of calling the model, it returns a message indicating that sensitive data was found.

If no sensitive data is found, the request is sent to the model as usual.

## Files

- `agent.py`: Contains the agent definition and the `check_before_model` callback.
- `dlp.py`: Contains the logic for interacting with the DLP API.
