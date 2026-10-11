"""Organisation-scoped record queries for a disposable SQLite fixture."""

import sqlite3


def list_records(
    connection: sqlite3.Connection, organisation_id: str, search: str = ""
) -> list[tuple]:
    return connection.execute(
        """SELECT id, organisation_id, title, created_at
           FROM records
           WHERE organisation_id = ? AND instr(title, ?) > 0
           ORDER BY created_at ASC, id ASC""",
        (organisation_id, search),
    ).fetchall()
