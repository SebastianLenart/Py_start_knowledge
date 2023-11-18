import sqlite3


class EntryRepository:
    def save(self, title, category, amount):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            print(category)
            cursor.execute("INSERT INTO entry ('category_id', 'name', 'amount') VALUES(?, ?, ?)",
                           (category, title, amount))
            connection.commit()

    def get_costs(self):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT entry.id, entry.name, entry.created_at, entry.amount, category.name FROM entry
LEFT JOIN category on entry.category_id = category.id
WHERE entry.amount < 0
ORDER BY created_at DESC""")
            return cursor.fetchall()

    def get_incomes(self):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT entry.id,entry.name, entry.created_at, entry.amount, category.name FROM entry
LEFT JOIN category on entry.category_id = category.id
WHERE entry.amount > 0
ORDER BY created_at DESC""")
            return cursor.fetchall()


class CategoryRepository:
    def get_by_name(self, name):
        print(f"Pobieram kategorie po nazwie {name}")
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name FROM category WHERE name = ?", (name,))
            return cursor.fetchone()


class ReportRepository:
    def get_saldo(self):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) as quantity, SUM(amount) as saldo FROM entry")
            return cursor.fetchall()[0]

    def get_by_category(self):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT
category.name,
COUNT(*) as quantity,
SUM(amount) as saldo
FROM
entry
LEFT JOIN category ON entry.category_id = category.id
GROUP BY category_id
ORDER BY created_at DESC""")
            return cursor.fetchall()
