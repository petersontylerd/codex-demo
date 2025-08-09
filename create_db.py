import sqlite3
import random

DB_PATH = "sample.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS transactions")
cur.execute(
    """
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL,
        quantity INTEGER,
        order_date TEXT
    )
    """
)

categories = ["A", "B", "C", "D"]
for i in range(1, 21):
    category = random.choice(categories)
    amount = round(random.uniform(10, 100), 2)
    quantity = random.randint(1, 5)
    order_date = f"2023-01-{random.randint(1, 28):02d}"
    cur.execute(
        "INSERT INTO transactions (id, category, amount, quantity, order_date) VALUES (?,?,?,?,?)",
        (i, category, amount, quantity, order_date),
    )

conn.commit()
conn.close()
