from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="Addition Server",
    host="0.0.0.0",  # only used for streamable-http
    port=8050,  # only used for streamable-http
    stateless_http=True,
)


# simple addition tool
@mcp.tool(name="add", description="Add two numbers")
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Run the server
if __name__ == "__main__":
    transport = "streamable-http"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "streamable-http":
        print("Running server with Streamable HTTP transport")
        mcp.run(transport="streamable-http")
    else:
        raise ValueError(f"transport protocol not know: {transport}")
