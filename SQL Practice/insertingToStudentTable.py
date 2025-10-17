
import sqlite3

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()

rollNo = int(input("Enter Roll No: "))
name = input("Enter Name : ")
city = input("Enter City : ")
deptno = int(input("Enter Department No: "))

cursor.execute(f"insert into students values({rollNo},'{name}','{city}',{deptno})")

conn.commit()

cursor.close()

conn.close()