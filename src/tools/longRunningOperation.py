# src/tools/longRunningOperation.py
import asyncio
from typing import Any
from mcp.server.fastmcp import Context
from core.server import mcp


@mcp.tool()
async def longRunningOperation(
    duration: int = 10,
    steps: int = 5,
    ctx: Context = None,
) -> str:
    """Demonstrates a long-running operation with progress notifications.

    Args:
        duration: Total duration of the operation in seconds (default: 10)
        steps: Number of progress steps to report (default: 5)

    Returns:
        Completion message with duration and steps info
    """
    step_duration = duration / steps

    for i in range(1, steps + 1):
        await asyncio.sleep(step_duration)
        if ctx is not None:
            await ctx.report_progress(
                progress=i,
                total=steps,
            )

    return f"Long running operation completed. Duration: {duration} seconds, Steps: {steps}."
