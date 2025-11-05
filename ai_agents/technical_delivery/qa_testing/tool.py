def log_bug(title: str, description: str, severity: str = "medium") -> str:
    """
    Simple bug logging mock: returns a bug id and next steps.
    """
    bug_id = abs(hash(title + description)) % 100000
    return f"Bug logged #{bug_id}: {title} (severity: {severity}). Assigned to QA team."
