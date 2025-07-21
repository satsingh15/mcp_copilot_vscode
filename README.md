### Building MCP Server using copilot and vscode

#### Steps, project initialization

1. mkdir mcp_copilot_vscode
2. uv init: This would create a bunch of files .python-version, pyproject.toml, uv.lock, main.py, .venv
3. uv add mcp[cli]==1.10.1
4. uv add python-dotenv
5. Code client-http.py and client-stdio.py
6. .\.venv\Scripts\activate  -> to run mcp 
7. mcp dev server.py: This install MCP inspector. Couple of things to ensure here is in stdio transport mode ensure command is uv and arguement is run --with mcp mcp run server.py.
Here is it does not matter whether we specify transport mechansim as streamable-http or stdio, MCP inspector in stdio mode is going to run server
8. in MCP inspector hit connect
9. in MCP inspector click on Tools, List tool, here we can see our add tool, test this out for your coursity
10. Create a folder .vscode, inside it create file mcp.json, it should give a button for 'Add Server' this button can also be used to register your toll with co-pilot but it did not work for me so we will add tool via toll option in chat
11. Click on tool option in co-pilot chat
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/toll_options.jpg?raw=true)

12. 
### Run mcp server
```bash
uv run server.py
```
