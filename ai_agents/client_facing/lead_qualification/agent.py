from google.adk.agents import Agent
from .tool import qualify_lead

lead_qualification_agent = Agent(
    name="lead_qualification_agent",
    model="gemini-2.0-flash",
    description="Screens incoming inquiries, determines scope/budget, qualifies leads.",
    instruction="Ask qualifying questions and return short qualification result.",
    tools=[qualify_lead],
)
