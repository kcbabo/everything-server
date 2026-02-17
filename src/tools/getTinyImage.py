# src/tools/getTinyImage.py
from mcp.types import ImageContent
from core.server import mcp

# A tiny 1x1 red pixel PNG, base64-encoded
TINY_IMAGE_DATA = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8"
    "z8BQDwADhQGAWjR9awAAAABJRU5ErkJggg=="
)


@mcp.tool()
def getTinyImage() -> list:
    """Returns a small test image to demonstrate image content in MCP tool responses.

    Returns:
        A base64-encoded 1x1 PNG image as image content
    """
    return [
        {
            "type": "text",
            "text": "Here is a tiny test image:",
        },
        ImageContent(
            type="image",
            data=TINY_IMAGE_DATA,
            mimeType="image/png",
        ),
    ]
