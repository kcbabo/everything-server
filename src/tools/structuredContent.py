# src/tools/structuredContent.py
from core.server import mcp


@mcp.tool()
def structuredContent(
    includeOptionalFields: bool = False,
) -> dict:
    """Returns structured content that conforms to a well-defined JSON schema.
    Demonstrates MCP's structured output / schema-validated tool responses.

    Args:
        includeOptionalFields: Whether to include optional fields in the response (default: False)

    Returns:
        A structured dict with schema-validated fields
    """
    result = {
        "name": "MCP Everything Server",
        "version": "1.0.0",
        "status": "running",
        "toolCount": 11,
        "supportsStreaming": True,
    }

    if includeOptionalFields:
        result.update(
            {
                "description": "A test MCP server that exercises all MCP protocol features.",
                "transportModes": ["stdio", "http"],
                "capabilities": [
                    "tools",
                    "resources",
                    "prompts",
                    "sampling",
                    "elicitation",
                    "roots",
                    "logging",
                ],
                "resourceCount": 100,
            }
        )

    return result
