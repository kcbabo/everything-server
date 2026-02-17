# src/tools/listRoots.py
from mcp.server.fastmcp import Context
from core.server import mcp


@mcp.tool()
async def listRoots(ctx: Context = None) -> str:
    """Lists the current MCP roots as reported by the connected MCP client.
    Roots define the filesystem or URI boundaries the client exposes to the server.

    Returns:
        A formatted list of roots provided by the client, or an indication
        that the client does not support roots
    """
    if ctx is None:
        return "Error: context not available for listing roots."

    try:
        result = await ctx.session.list_roots()

        if result is None or not result.roots:
            return "The client reported no roots (roots may not be supported or none are configured)."

        lines = [f"Client roots ({len(result.roots)} total):\n"]
        for root in result.roots:
            name = getattr(root, "name", None) or "(unnamed)"
            uri = getattr(root, "uri", str(root))
            lines.append(f"  - {name}: {uri}")

        return "\n".join(lines)

    except (AttributeError, NotImplementedError):
        return "Roots listing is not supported by this MCP client."
    except Exception as e:
        return f"Error listing roots: {str(e)}"
