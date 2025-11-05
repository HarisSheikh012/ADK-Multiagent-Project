from google.adk.agents import Agent
from .tool import draft_blog

content_marketing_agent = Agent(
    name="content_marketing_agent",
    model="gemini-2.0-flash",
    description="Drafts blog posts on IT trends, case studies, AI innovations.",
    instruction="Produce topic-focused blog drafts and short outlines.",
    tools=[draft_blog],
    sub_agents=[], 
)
