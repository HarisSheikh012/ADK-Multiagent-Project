from google.adk.agents import Agent
from .tool import scope_project

project_scoping_agent = Agent(
    name="project_scoping_agent",
    model="gemini-2.0-flash",
    description="Gather initial requirements and provide rough estimates for web/app projects.",
    instruction="Ask for requirements, tech preferences, timelines, and provide a simple estimate.",
    tools=[scope_project],
)
