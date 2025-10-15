from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("My MCP Server")

@mcp.custom_route("/", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
# By setting prefix="", the router's paths are added from the application's root.
    mcp.run(transport="http", port=8080, host="0.0.0.0")