import os
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StdioConnectionParams,
    StdioServerParameters,
)

# Define database path
DB_PATH = os.path.join(os.path.dirname(__file__), "adk_agents.db")

# Ensure folder exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# ✅ Correct: use full npx command path as a list (Pydantic fix below)
connection_params = StdioConnectionParams(
    server_params=StdioServerParameters(
        command="npx",  # executable
        args=["sqlite-mcp-server", "--db_path", DB_PATH],  # arguments
    )
)

# Initialize MCP toolset
database_mcp_toolset = MCPToolset(connection_params=connection_params)
