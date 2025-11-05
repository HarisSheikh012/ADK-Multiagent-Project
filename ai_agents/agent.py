import os
import logging
from google.adk.agents import Agent

# ---------- Import Subagents ----------
# Client-facing
from .client_facing.lead_qualification.agent import lead_qualification_agent
from .client_facing.project_scoping.agent import project_scoping_agent
from .client_facing.client_onboarding.agent import client_onboarding_agent
from .client_facing.client_communication.agent import client_communication_agent

# Technical & delivery
from .technical_delivery.technical_presales.agent import technical_presales_agent
from .technical_delivery.seo_audit.agent import seo_audit_agent
from .technical_delivery.qa_testing.agent import qa_testing_agent
from .technical_delivery.documentation.agent import documentation_agent

# Marketing & content
from .marketing_content.content_marketing.agent import content_marketing_agent
from .marketing_content.social_media.agent import social_media_agent
from .marketing_content.seo_content.agent import seo_content_agent

# Operations
from .operations.resource_allocation.agent import resource_allocation_agent
from .operations.invoice_billing.agent import invoice_billing_agent
from .operations.vendor_management.agent import vendor_management_agent


# ---------------- Root Agent ----------------
root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="Central AI Operations Agent managing client, technical, marketing, and operations workflows.",
    instruction="""
        You are the root coordinator. Route requests to the appropriate sub-agent:
        - Client-facing: lead qualification, scoping, onboarding, communication.
        - Technical & delivery: pre-sales, SEO audits, QA, documentation.
        - Marketing & content: content marketing, social media, SEO content.
        - Operations: resource allocation, invoices, vendor management.
        If a task needs file operations, use the MCP filesystem tool (if available).
        If unsure, ask a clarifying question.
    """,
    sub_agents=[
        lead_qualification_agent,
        project_scoping_agent,
        client_onboarding_agent,
        client_communication_agent,
        technical_presales_agent,
        seo_audit_agent,
        qa_testing_agent,
        documentation_agent,
        content_marketing_agent,
        social_media_agent,
        seo_content_agent,
        resource_allocation_agent,
        invoice_billing_agent,
        vendor_management_agent,
    ],
)


# ---------------- Safe Peer Links (for visualization) ----------------
try:
    # Client-Facing Flow
    lead_qualification_agent.sub_agents.append(project_scoping_agent)
    project_scoping_agent.sub_agents.append(client_onboarding_agent)
    client_onboarding_agent.sub_agents.append(client_communication_agent)

    # Technical Flow
    technical_presales_agent.sub_agents.append(seo_audit_agent)
    seo_audit_agent.sub_agents.append(qa_testing_agent)
    qa_testing_agent.sub_agents.append(documentation_agent)

    # Marketing Flow
    content_marketing_agent.sub_agents.append(social_media_agent)
    social_media_agent.sub_agents.append(seo_content_agent)

    # Operations Flow
    resource_allocation_agent.sub_agents.append(invoice_billing_agent)
    invoice_billing_agent.sub_agents.append(vendor_management_agent)

    # Cross-domain visualization connections (no loops)
    client_communication_agent.sub_agents.append(invoice_billing_agent)
    qa_testing_agent.sub_agents.append(content_marketing_agent)
    content_marketing_agent.sub_agents.append(client_communication_agent)
    resource_allocation_agent.sub_agents.append(project_scoping_agent)

    logging.info("✅ Visualization peer-to-peer links added (safe, non-recursive).")

except Exception as e:
    logging.warning(f"⚠️ Peer linking skipped due to error: {e}")


# ---------------- Notes ----------------
"""
💡 Visualization Guide:

Run:
    google-adk visualize agents

You’ll now see:
- Agents connected to each other (A → B) lines in the image event.
- No recursion errors.
- The diagram forms a realistic workflow network:
    Lead Qualification → Project Scoping → Onboarding → Communication
    Technical Presales → SEO Audit → QA Testing → Documentation
    Content Marketing → Social Media → SEO Content
    Resource Allocation → Billing → Vendor Management
    + cross-links between communication, marketing, and operations
"""
