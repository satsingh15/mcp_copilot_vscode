import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client



async def main():
    server_params = StdioServerParameters(
        command="python",  # The command to run your server so we do not have to run mcp server again
        args=["server.py"],  
    )

    # Connect to the server
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tool_list = await session.list_tools()
            print("Available tools listed below:")
            for tool in tool_list.tools:
                print(f"|--> {tool.name}: {tool.description}")

            # Call addition tool
            result = await session.call_tool("add", arguments={"a": 4, "b": -3})
            print(f"Call tool result 4 + -3 = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
