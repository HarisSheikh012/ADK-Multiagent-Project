import sqlite3
import os

DB_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../mcp_server/adk_agents.db")
)


def project_update(
    project_id: str, status: str = "in progress", notes: str = ""
) -> str:
    """
    Store project communication in database and return formatted update.
    """
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Create table if missing
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS client_communications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id TEXT NOT NULL,
            status TEXT NOT NULL,
            notes TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    cursor.execute(
        "INSERT INTO client_communications (project_id, status, notes) VALUES (?, ?, ?)",
        (project_id, status, notes),
    )
    conn.commit()
    conn.close()
    return f"Project {project_id}: Status = {status}. Notes: {notes or 'No additional notes.'} (Saved to DB)"
