def scope_project(summary: str, complexity: str = "medium") -> str:
    """
    Return a rough scoping estimate based on high-level summary and complexity.
    """
    base = 1000
    if complexity.lower() == "low":
        cost = base * 1.0
        days = 7
    elif complexity.lower() == "high":
        cost = base * 5.0
        days = 45
    else:
        cost = base * 2.5
        days = 21
    return (
        f"Estimated cost: ${cost:.0f}, timeline approx {days} days. Summary: {summary}"
    )
