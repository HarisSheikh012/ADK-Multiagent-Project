from google.adk.agents import Agent
from .tool import start_onboarding

client_onboarding_agent = Agent(
    name="client_onboarding_agent",
    model="gemini-2.0-flash",
    description="Manage onboarding: collect docs, NDA, briefs and assets.",
    instruction="Guide new clients through onboarding steps and confirm document completion.",
    tools=[start_onboarding],
)
