# ADK Walkthrough

***Tested with Google ADK 1.16.0***

This project contains a series of examples demonstrating how to use the Google Agent Development Kit (ADK). Each folder contains a different agent configuration, showcasing a specific feature of the ADK.

## Execution

You can try the agents by adding a `.env` file to each agents folder with the following information:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE/FALSE
GOOGLE_CLOUD_PROJECT=PROJECT_ID if VERTEXAI == TRUE
GOOGLE_CLOUD_LOCATION=global
GOOGLE_API_KEY=Key if VERETXAI == FALSE
```

After that, run the following:

1. Create a virtual environment, e.g. with `python -m venv .venv` and activate it with `source .venv/bin/activate`.
2. Install requirements, e.g. with `pip install -r requirements.txt`
3. Run ADK Web with `adk web`

## Agents

### [001 - LlmAgent](https://github.com/schenkfab/adk-demos/tree/main/001%20-%20LlmAgent)

This agent demonstrates the fundamental `LlmAgent`. It shows how to define an agent with a name, description, model, and instruction. It also covers adding a `static_instruction` for context caching and defining an `output_schema` for structured output.

### [002 - Sequential Agent](https://github.com/schenkfab/adk-demos/tree/main/002%20-%20Sequential%20Agent)

This example introduces the `SequentialAgent`, which executes a series of sub-agents in a predefined order. The included agent first greets the user and then says goodbye, showcasing a simple sequential workflow.

### [003 - Parallel Agent](https://github.com/schenkfab/adk-demos/tree/main/003%20-%20Parallel%20Agent)

This agent demonstrates the `ParallelAgent`, which runs multiple sub-agents concurrently. The example features three agents that greet the user in different languages simultaneously, illustrating how to perform parallel tasks.

### [004 - Loop Agent](https://github.com/schenkfab/adk-demos/tree/main/004%20-%20Loop%20Agent)

This example shows how to use the `LoopAgent` to run a sub-agent multiple times. The agent in this folder will greet the user in German three times in a row.

### [004-1 - Loop Agent ADVANCED](https://github.com/schenkfab/adk-demos/tree/main/004-1%20-%20Loop%20Agent%20ADVANCED)

This more advanced `LoopAgent` example demonstrates a content creation and review loop. A `writer_agent` generates an article, and a `check_agent` verifies if it meets a specific word count. The loop continues until the condition is met or the maximum number of iterations is reached, using a custom `exit_loop` tool to terminate the process.

### [005 - Tools](https://github.com/schenkfab/adk-demos/tree/main/005%20-%20Tools)

This agent demonstrates how to create and use custom tools. A `get_words` tool is defined to count the words in a text, and a `check_agent` uses this tool to validate the length of an article created by a `writer_agent`.

### [006 - AgentTool](https://github.com/schenkfab/adk-demos/tree/main/006%20-%20AgentTool)

This example illustrates how to use an `AgentTool`, which allows one agent to use another agent as a tool. The `root_agent` in this example uses a `check_agent` (which itself has a `get_words` tool) to verify the word count of a generated article.

### [007 - BuiltIn Tools](https://github.com/schenkfab/adk-demos/tree/main/007%20-%20BuiltIn%20Tools)

This agent shows how to use the built-in `google_search` tool. The agent is configured to act as a search specialist, demonstrating how to integrate pre-built functionalities.

### [008 - MCP Tools](https://github.com/schenkfab/adk-demos/tree/main/008%20-%20MCP%20Tools)

This example demonstrates the use of MCP (Multiple-Context Prompting) tools. The agent connects to an external MCP server using an `MCPToolset` to generate a custom greeting, showcasing how to extend agent capabilities with external services.

### [009 - Application Integration](https://github.com/schenkfab/adk-demos/tree/main/009%20-%20Application%20Integration)

This agent demonstrates how to use the `ApplicationIntegrationToolset` to connect to a Google Cloud Application Integration. This allows the agent to trigger integrations and use them as tools.

### [010 - DLP Callback](https://github.com/schenkfab/adk-demos/tree/main/010%20-%20DLP%20Callback)

This agent uses a `Google Cloud Data Loss Prevention API` to check for PII in a given text. The tool is configured with a callback to the `LlmAgent` to redact the PII.