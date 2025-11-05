def schedule_post(content: str, platform: str = "twitter") -> str:
    """
    Mock scheduling: returns scheduled time and platform.
    """
    return f"Scheduled post to {platform}: '{content[:60]}...' (scheduled for tomorrow 09:00)"
