def vendor_coord(vendor_name: str, task: str, due: str) -> str:
    return (
        f"Created task for vendor {vendor_name}: {task} (due {due}). Notified vendor."
    )
