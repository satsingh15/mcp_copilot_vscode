### Building MCP Server using copilot and vscode
Demo illustrates how to build a simple mcp server and connect it co-pilot
We are using uv instead of pip. uv is faster, simpler than pip but is funded by VC, so it might pull a redis on us.

#### Steps, project initialization
1. Basic project files creation. 
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

5. in MCP inspector hit connect, in MCP inspector click on Tools, List tool, here we can see our add tool, test this out for your coursity may be run add tool
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/3.jpg?raw=true)

6. You can also look at streamable http option, note the url
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/5.jpg?raw=true)

7. Create a folder .vscode, inside it create file mcp.json, it should give a button for 'Add Server' this button can also be used to register your toll with co-pilot but it did not work for me so we will add tool via tool option in chat. Also ensure mcp server is running. 
You can also run below command to run mcp server.
```bash
uv run server.py
```
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json1.jpg?raw=true)


8. Click on tool option in co-pilot chat

![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/tool_options.jpg?raw=true)


9. Choose http 

![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json2.jpg?raw=true)

10. enter the address where mcp server is running usually it will http:0.0.0.0:8050/mcp or http:localhost:8050/mcp, prefer http:0.0.0.0:8050/mcp, since it will be added in mcp.json
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json3.jpg?raw=true)

11. Name your mcp server
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json4.jpg?raw=true)


12. Below content should be populated in mcp.json. This content helps co-pilot to recognize tool.
More info here: 
https://code.visualstudio.com/docs/copilot/chat/mcp-servers
https://learn.microsoft.com/en-us/azure/app-service/tutorial-ai-model-context-protocol-server-dotnet

![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json6.jpg?raw=true)





13. Exciting moment now, try our tool in co-pilot chat
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json7.jpg?raw=true)



14. Hit continue, Voila
![alt text](https://github.com/satsingh15/mcp_copilot_vscode/blob/main/images/mcp.json8.jpg?raw=true)

