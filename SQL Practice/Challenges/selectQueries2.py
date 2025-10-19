
# find students Names from 'CSE' Department

import sqlite3 

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

rows = cursor.execute('select name from students s,dept d where s.deptno = d.deptno and d.dname = "CSE"')

tuples = rows.fetchall()

for t in tuples: 
    print(t)

cursor.close()
conn.close()