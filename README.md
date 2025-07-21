### Building MCP Server using copilot and vscode

#### Steps, project initialization

1. Basic project files creation. We are using uv instead of pip. uv is faster, simpler than pip but is funded by VC, so it might pull a redis on us.
```bash
mkdir mcp_copilot_vscode
uv init
uv add mcp[cli]==1.10.1
uv add python-dotenv
```
2. uv init: This would create a bunch of files .python-version, pyproject.toml, uv.lock, main.py, .venv
3. Code client-http.py and client-stdio.py
4. run below commands. 1st command is for venv. mcp dev server.py installs MCP inspector. Couple of things to ensure here is in stdio transport mode ensure command is uv and arguement is run --with mcp mcp run server.py
```bash
.\.venv\Scripts\activate
mcp dev server.py
```
This install MCP inspector. MCP inspector is great for debugging. 
Couple of things to ensure here is in stdio transport mode ensure command is uv and argument is run --with mcp mcp run server.py.
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/4.jpg?raw=true)
in MCP inspector hit connect, in MCP inspector click on Tools, List tool, here we can see our add tool, test this out for your coursity
May be run add tool
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/3.jpg?raw=true)
You can also look at streamable http option, note the url
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/5.jpg?raw=true)

5. Create a folder .vscode, inside it create file mcp.json, it should give a button for 'Add Server' this button can also be used to register your toll with co-pilot but it did not work for me so we will add tool via tool option in chat
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json1.jpg?raw=true)

6. Click on tool option in co-pilot chat
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/tool_options.jpg?raw=true)

![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json2.jpg?raw=true)

![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json3.jpg?raw=true)

![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json4.jpg?raw=true)

![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json5.jpg?raw=true)


![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json6.jpg?raw=true)

![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json7.jpg?raw=true)


![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json8.jpg?raw=true)

