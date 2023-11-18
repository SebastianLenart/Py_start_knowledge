CREATE TABLE category (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
)

CREATE TABLE entry(
id INTEGER PRIMARY KEY AUTOINCREMENT,
category_id INTEGER,
name TEXT,
amount FLOAT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

SELECT entry.id, entry.created_at, entry.amount, category.name FROM entry
LEFT JOIN category on entry.category_id = category.id
ORDER BY created_at DESC;

SELECT
category.name
COUNT(*) as quantity,
SUM(amount) as saldo
FROM
entry
LEFT JOIN category ON entry.category_id = category.id
GROUP BY category_id
ORDER BY created_at DESC;


SELECT COUNT(*) as quantity, SUM(amount) as saldo FROM entry;


