# src/tools/printEnv.py
import os
from core.server import mcp


@mcp.tool()
def printEnv() -> str:
    """Prints all current environment variables.
    Useful for debugging server configuration and available environment context.

    Returns:
        A formatted list of all environment variables
    """
    env_vars = os.environ

    if not env_vars:
        return "No environment variables found."

    lines = ["Current environment variables:\n"]
    for key in sorted(env_vars.keys()):
        lines.append(f"  {key}={env_vars[key]}")

    return "\n".join(lines)
