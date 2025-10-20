
# Delete Department 50

import sqlite3 

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

cursor.execute('delete from dept where deptno = 50')

conn.commit()

cursor.close()

conn.close()