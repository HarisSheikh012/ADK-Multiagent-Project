def qualify_lead(client_name: str, project_description: str, budget: float) -> str:
    """
    Basic qualification logic:
      - budget < 500 -> low
      - 500 <= budget < 2000 -> moderate
      - >=2000 -> qualified
    """
    if budget < 500:
        return f"Lead '{client_name}' NOT qualified: budget ${budget} too low."
    if 500 <= budget < 2000:
        return f"Lead '{client_name}' may be qualified: budget ${budget}. Request more details."
    return f"Lead '{client_name}' qualified: budget ${budget}. Proceed to sales."
