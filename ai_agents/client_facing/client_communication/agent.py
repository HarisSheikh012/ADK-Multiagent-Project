from google.adk.agents import Agent
from ...mcp_server.database_server import database_mcp_toolset
from .tool import project_update

client_communication_agent = Agent(
    name="client_communication_agent",
    model="gemini-2.0-flash",
    description="Handles client updates, logs communication history, and provides project status updates.",
    instruction="Respond with clear updates and store communications in the database.",
    tools=[project_update, database_mcp_toolset],
)
