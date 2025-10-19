
# Find Civil Department students not from MUM

import sqlite3 

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

rows = cursor.execute('select * from students where deptno = 30 except select * from students where city = "MUM"')

tuples = rows.fetchall()

for t in tuples:
    print(t)

cursor.close()
conn.close()

