def allocate_resource(project_skills: list, team: list) -> str:
    """
    team is a list of dicts: {name: str, skills: [..], availability: bool}
    This mock returns the first matching available resource.
    """
    for member in team:
        if member.get("availability") and set(project_skills).issubset(
            set(member.get("skills", []))
        ):
            return f"Assigned {member['name']} to the project."
    return "No available resource found that matches requirements."
