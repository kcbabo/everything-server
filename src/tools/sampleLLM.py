# src/tools/sampleLLM.py
from mcp.server.fastmcp import Context
from core.server import mcp


@mcp.tool()
async def sampleLLM(
    prompt: str,
    maxTokens: int = 100,
    ctx: Context = None,
) -> str:
    """Demonstrates LLM sampling capability using the MCP sampling feature.
    Requests the MCP client to sample from an LLM on behalf of this tool.

    Args:
        prompt: The prompt to send to the LLM
        maxTokens: Maximum number of tokens to generate (default: 100)

    Returns:
        The generated LLM response text
    """
    if ctx is None:
        return "Error: context not available for LLM sampling."

    result = await ctx.sample(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=maxTokens,
    )

    # result is a CreateMessageResult; extract the text content
    if hasattr(result, "content"):
        content = result.content
        if hasattr(content, "text"):
            return f"LLM sampling result:\n{content.text}"
        return f"LLM sampling result:\n{str(content)}"

    return f"LLM sampling result:\n{str(result)}"
