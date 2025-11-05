from google.adk.agents import Agent
from .tool import create_doc

documentation_agent = Agent(
    name="documentation_agent",
    model="gemini-2.0-flash",
    description="Creates technical docs, user guides, and maintains project wikis.",
    instruction="Produce clear, actionable documentation and short how-to guides.",
    tools=[create_doc],
    sub_agents=[], 
)
