import sqlite3
from typing import Dict

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone_number TEXT NOT NULL,
                    food_rating INTEGER NOT NULL,
                    cleanliness_rating INTEGER NOT NULL,
                    extra_comments TEXT NOT NULL
                )
            """)
            conn.commit()

    async def save_review(self, data: Dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                INSERT INTO reviews (name, phone_number, food_rating, cleanliness_rating, extra_comments)
                VALUES (?, ?, ?, ?, ?)
            """, (
                data['name'],
                data['phone_number'],
                data['food_rating'],
                data['cleanliness_rating'],
                data['extra_comments']
            ))
            conn.commit()
