
# Find Numbers of 'ECE' Students from residing in each city

import sqlite3 

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

rows = cursor.execute('select city,count(city) from students where deptno = 20 group by city')

tuples = rows.fetchall()

for t in tuples:
    print(t)

cursor.close()

conn.close()