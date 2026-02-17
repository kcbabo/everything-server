# src/tools/startElicitation.py
from mcp.server.fastmcp import Context
from core.server import mcp


@mcp.tool()
async def startElicitation(
    message: str = "Please provide your name:",
    ctx: Context = None,
) -> str:
    """Demonstrates MCP elicitation by requesting structured input from the user
    via the MCP client. Elicitation allows servers to interactively ask users
    for information during a tool call.

    Args:
        message: The prompt message to display to the user (default: "Please provide your name:")

    Returns:
        The user's response from the elicitation, or an error if not supported
    """
    if ctx is None:
        return "Error: context not available for elicitation."

    try:
        result = await ctx.elicit(
            message=message,
            schema={
                "type": "object",
                "properties": {
                    "response": {
                        "type": "string",
                        "description": "Your response",
                    }
                },
                "required": ["response"],
            },
        )

        if result is None:
            return "Elicitation was cancelled or not supported by the client."

        response_value = result.get("response", str(result))
        return f"Elicitation result: {response_value}"

    except (AttributeError, NotImplementedError):
        return "Elicitation is not supported by this MCP client."
    except Exception as e:
        return f"Elicitation error: {str(e)}"
