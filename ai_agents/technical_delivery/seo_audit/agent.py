from google.adk.agents import Agent
from .tool import run_seo_audit

seo_audit_agent = Agent(
    name="seo_audit_agent",
    model="gemini-2.0-flash",
    description="Performs an initial website SEO audit and returns suggestions.",
    instruction="Provide a short SEO audit summary and top 5 improvement suggestions.",
    tools=[run_seo_audit],
    sub_agents=[], 
)
