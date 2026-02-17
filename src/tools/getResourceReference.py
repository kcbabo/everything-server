# src/tools/getResourceReference.py
from core.server import mcp


@mcp.tool()
def getResourceReference(resourceId: int) -> list:
    """Returns a resource reference that can be used by MCP clients to fetch a resource.
    The resource ID must be between 1 and 100.

    Args:
        resourceId: ID of the resource to reference (1-100)

    Returns:
        A list containing a text introduction, an embedded resource reference,
        and instructions for using the resource URI
    """
    if resourceId < 1 or resourceId > 100:
        return [
            {
                "type": "text",
                "text": f"Error: resourceId must be between 1 and 100, got {resourceId}.",
            }
        ]

    uri = f"test://static/resource/{resourceId}"

    return [
        {
            "type": "text",
            "text": f"Here is a reference to resource {resourceId}:",
        },
        {
            "type": "resource",
            "resource": {
                "uri": uri,
                "mimeType": "text/plain" if resourceId % 2 == 0 else "application/octet-stream",
                "text": f"Resource {resourceId}" if resourceId % 2 == 0 else None,
            },
        },
        {
            "type": "text",
            "text": f"You can use the URI '{uri}' to fetch this resource directly.",
        },
    ]
