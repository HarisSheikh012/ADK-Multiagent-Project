from google.adk.agents import Agent
from .tool import answer_technical

technical_presales_agent = Agent(
    name="technical_presales_agent",
    model="gemini-2.0-flash",
    description="Answers technical questions about AI, mobile, web, and SEO capabilities.",
    instruction="Provide concise, accurate technical answers and reference implementation options.",
    tools=[answer_technical],
    sub_agents=[], 
)
