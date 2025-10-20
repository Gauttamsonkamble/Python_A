
# update Department name to 'IT' for deptno 50 

import sqlite3 

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

cursor.execute('update dept set dname = "IT" where deptno = 50 ')

conn.commit()

cursor.close()

conn.close()