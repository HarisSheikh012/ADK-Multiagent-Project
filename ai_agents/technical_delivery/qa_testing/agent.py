from google.adk.agents import Agent
from .tool import log_bug

qa_testing_agent = Agent(
    name="qa_testing_agent",
    model="gemini-2.0-flash",
    description="Coordinates QA, logs bugs, and manages testing schedules.",
    instruction="Record bug reports and provide testing status summaries.",
    tools=[log_bug],
    sub_agents=[], 
)
