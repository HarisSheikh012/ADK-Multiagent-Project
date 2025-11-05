from google.adk.agents import Agent
from .tool import create_invoice

invoice_billing_agent = Agent(
    name="invoice_billing_agent",
    model="gemini-2.0-flash",
    description="Creates invoices, sends payment reminders, and answers billing queries.",
    instruction="Generate invoices and polite payment reminders.",
    tools=[create_invoice],
    sub_agents=[], 
)
