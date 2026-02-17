# src/tools/annotatedMessage.py
from typing import Literal
from core.server import mcp


@mcp.tool()
def annotatedMessage(
    messageType: Literal["error", "success", "debug"] = "success",
    includeImage: bool = False,
) -> list:
    """Demonstrates different annotation patterns for MCP tool responses.
    Returns content with metadata annotations based on the message type.

    Args:
        messageType: Type of message to demonstrate - "error", "success", or "debug"
        includeImage: Whether to include an example image in the response (default: False)

    Returns:
        Annotated content demonstrating MCP annotation capabilities
    """
    # Map message types to annotation priorities and audiences
    annotations_map = {
        "error": {
            "audience": ["user", "assistant"],
            "priority": 1.0,
            "text": "This is an error message. Something went wrong.",
        },
        "success": {
            "audience": ["user"],
            "priority": 0.5,
            "text": "Operation completed successfully.",
        },
        "debug": {
            "audience": ["assistant"],
            "priority": 0.1,
            "text": "Debug info: internal state looks nominal.",
        },
    }

    info = annotations_map.get(messageType, annotations_map["success"])

    content = [
        {
            "type": "text",
            "text": info["text"],
            "annotations": {
                "audience": info["audience"],
                "priority": info["priority"],
            },
        },
        {
            "type": "text",
            "text": f"Message type: {messageType} | Priority: {info['priority']} | Audience: {', '.join(info['audience'])}",
            "annotations": {
                "audience": ["assistant"],
                "priority": 0.0,
            },
        },
    ]

    if includeImage:
        # Tiny 1x1 transparent PNG
        tiny_png = (
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk"
            "YPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
        )
        content.append(
            {
                "type": "image",
                "data": tiny_png,
                "mimeType": "image/png",
                "annotations": {
                    "audience": ["user"],
                    "priority": 0.3,
                },
            }
        )

    return content
