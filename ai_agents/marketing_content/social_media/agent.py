from google.adk.agents import Agent
from .tool import schedule_post

social_media_agent = Agent(
    name="social_media_agent",
    model="gemini-2.0-flash",
    description="Schedules posts, responds to comments, and engages community.",
    instruction="Create short, engaging social posts and suggested post times.",
    tools=[schedule_post],
    sub_agents=[], 
)