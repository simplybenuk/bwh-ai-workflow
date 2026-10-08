"""Baseline query contracts. Evaluation tasks add their own regression checks."""

import sqlite3
import unittest
from pathlib import Path

from records import list_records


class RecordsTests(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.addCleanup(self.connection.close)
        self.connection.executescript(
            Path(__file__).with_name("schema.sql").read_text(encoding="utf-8")
        )
        self.connection.executemany(
            "INSERT INTO records VALUES (?, ?, ?, ?)",
            [
                (1, "alpha", "Field visit", "2026-10-01T09:00:00Z"),
                (2, "alpha", "Field visit follow-up", "2026-10-03T09:00:00Z"),
                (3, "alpha", "Office note", "2026-10-03T09:00:00Z"),
                (4, "beta", "Field visit", "2026-10-05T09:00:00Z"),
                (5, "alpha", "Visitor's note", "2026-10-02T09:00:00Z"),
            ],
        )

    def test_organisation_isolation_and_fields(self):
        rows = list_records(self.connection, "alpha")
        self.assertEqual({row[0] for row in rows}, {1, 2, 3, 5})
        self.assertTrue(all(row[1] == "alpha" and len(row) == 4 for row in rows))

    def test_literal_title_search(self):
        rows = list_records(self.connection, "alpha", "Field visit")
        self.assertEqual({row[0] for row in rows}, {1, 2})

    def test_quotes_are_data(self):
        rows = list_records(self.connection, "alpha", "Visitor's")
        self.assertEqual([row[0] for row in rows], [5])
        self.assertEqual(list_records(self.connection, "alpha", "' OR 1=1 --"), [])

    def test_missing_organisation_has_no_records(self):
        self.assertEqual(list_records(self.connection, "missing"), [])


if __name__ == "__main__":
    unittest.main()
