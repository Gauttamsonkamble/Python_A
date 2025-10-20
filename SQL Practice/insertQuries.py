
# Insert new Department 'Chem' deptno 50 

import sqlite3 

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

cursor.execute('insert into dept values(50,"Chem")')

conn.commit()

cursor.close()

conn.close()