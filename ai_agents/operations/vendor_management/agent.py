from google.adk.agents import Agent
from .tool import vendor_coord

vendor_management_agent = Agent(
    name="vendor_management_agent",
    model="gemini-2.0-flash",
    description="Coordinates with third-party tools, hosting providers, and freelancers.",
    instruction="Track vendor tasks, follow up with due dates, and summarize vendor status.",
    tools=[vendor_coord],
    sub_agents=[], 
)
