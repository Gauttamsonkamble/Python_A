
# Find Dept Having strength more than strength of 'ECE' Dept 

import sqlite3 

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

rows = cursor.execute('select deptno, count(*) from students group by deptno having count(*) > (select count(*) from students where deptno = 20)')

tuples = rows.fetchall()

for t in tuples:
    print(t)

cursor.close()
conn.close()