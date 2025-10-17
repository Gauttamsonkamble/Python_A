
import sqlite3

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

# cursor.execute('insert into dept values(10,"CSE")')

deptno = int (input('Enter Department NO: '))
deptName = input("Enter Department Name: ")

cursor.execute(f'insert into dept values({deptno},"{deptName}")')

conn.commit()

cursor.close()
conn.close()