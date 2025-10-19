
# Find all the cities where students are living

import sqlite3 

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

rows = cursor.execute('select distinct city from students')

tuples = rows.fetchall()

for t in tuples:
    print(t)

# print(tuples)
cursor.close()

conn.close()

