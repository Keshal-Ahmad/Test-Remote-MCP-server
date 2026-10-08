import random
from fastmcp import FastMCP
import json

# Create a FastMCP server instance
mcp = FastMCP(name="Remote Server")

@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll n_dice 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def divide_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a / b

#resource server information
@mcp.resource("info://server")
def server_info()->str:
    "It provide information about "
    info={
        "Data":"simple caluclator",
        "version":"1.0.9",
        "descrption":"A basic MCP server",
        "tools":["divide_random","roll_dice"]
    }
    return json.dumps(info,indent=2)



if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)

    # fastmcp run server.py --transport http --host 0.0.0.0 --port 8000