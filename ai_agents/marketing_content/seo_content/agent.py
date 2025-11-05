from google.adk.agents import Agent
from .tool import optimize_content

seo_content_agent = Agent(
    name="seo_content_agent",
    model="gemini-2.0-flash",
    description="Researches keywords, optimizes content, monitors rankings.",
    instruction="Provide keyword suggestions and on-page optimization tips.",
    tools=[optimize_content],
    sub_agents=[], 
)
