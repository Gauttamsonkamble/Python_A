
import sqlite3

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

rows = cursor.execute('select * from dept')

# t = row.fetchone()

tuples = rows.fetchall()

# print(tuples)

for t in tuples:
    print(t[0], t[1])

cursor.close()

conn.close()