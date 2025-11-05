from google.adk.agents import Agent
from .tool import allocate_resource

resource_allocation_agent = Agent(
    name="resource_allocation_agent",
    model="gemini-2.0-flash",
    description="Matches developers/designers to projects based on skills and availability.",
    instruction="Suggest the best resource match given skills and project needs.",
    tools=[allocate_resource],
    sub_agents=[], 
)
