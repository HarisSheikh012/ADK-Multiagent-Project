def run_seo_audit(url: str) -> str:
    """
    Mock SEO audit: returns suggestions. (In prod you'd fetch & analyze)
    """
    suggestions = [
        "Add descriptive title tags",
        "Ensure pages have meta descriptions",
        "Improve mobile responsiveness",
        "Compress images",
        "Add structured data for key pages",
    ]
    return f"SEO audit for {url}: Top suggestions: {', '.join(suggestions)}"
