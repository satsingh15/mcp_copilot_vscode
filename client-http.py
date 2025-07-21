import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client



async def main():
    # Connect to the server using transport Streamable HTTP
    async with streamablehttp_client("http://localhost:8050/mcp") as (
        read_stream,
        write_stream,
        get_session_id,
    ):
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
