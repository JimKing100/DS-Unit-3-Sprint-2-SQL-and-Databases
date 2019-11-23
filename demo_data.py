import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

query1 = """
CREATE TABLE IF NOT EXISTS demo (s varchar(255), x int, y int);
"""
curs1 = conn.cursor()
curs1.execute(query1)

query2 = """
DELETE FROM demo
"""

curs2 = conn.cursor()
curs2.execute(query2)

query3 = """
INSERT INTO demo (s, x, y) values ('g', '3', '9'),
                                  ('v', '5', '7'),
                                  ('f', '8', '7');
"""

curs3 = conn.cursor()
curs3.execute(query3)

query4 = """
SELECT COUNT(*) FROM demo;
"""

query5 = """
SELECT COUNT(*) FROM demo
WHERE x >= 5 AND y >= 5;
"""

query6 = """
SELECT COUNT(DISTINCT(y)) FROM demo;
"""

curs4 = conn.cursor()
print(curs4.execute(query4).fetchall())

curs5 = conn.cursor()
print(curs5.execute(query5).fetchall())

curs6 = conn.cursor()
print(curs6.execute(query6).fetchall())
