def draft_blog(topic: str, audience: str = "developers") -> str:
    """
    Return a short blog draft paragraph and suggested headings.
    """
    headings = ["Intro", "Problem", "Solution", "Case Study", "Conclusion"]
    paragraph = (
        f"{topic} is reshaping the {audience} landscape. Here's a short overview..."
    )
    return f"Headings: {', '.join(headings)}\n\nDraft: {paragraph}"
