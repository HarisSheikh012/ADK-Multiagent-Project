def start_onboarding(client_name: str, email: str) -> str:
    """
    Returns a checklist and next steps for client onboarding.
    """
    checklist = [
        "Sign NDA",
        "Share project brief",
        "Provide branding assets",
        "Share access credentials (if any)",
    ]
    return f"Onboarding started for {client_name}. Sent email to {email}. Checklist: {', '.join(checklist)}"
