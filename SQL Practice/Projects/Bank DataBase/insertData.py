
import sqlite3 

conn = sqlite3.connect('bank.db')

cursor = conn.cursor()

# Customers 
cursor.execute(''' insert into customers values (110,'anil','Mumbai','anil@gmail.com'),(111,'smith','Delhi','smith@example.com'),(112,'Ramesh','Mumbai','ramesh@gmail.com'),(113,'Khan','Delhi','khan@example.com') ''')

# Accounts 
cursor.execute(''' insert into accounts values (101,110,'Saving',2500.00),
                                               (102,111,'Checking',1200.50),
                                               (103,112,'Saving',1500.00),
                                                (104,113,'Checking',1700.00)
#                 ''')

#Transaction
cursor.execute(''' insert into Transanction values 
                   (1,101,'Deposit',500.00,'2025-07-04'),
                   (2,102,'withdrawal',100.00,'2025-07-05'),
                   (3,103,'Deposit',300.00,'2025-07-06'),
                   (4,104,'withdrawal',200.00,'2025-07-09'),
                   (5,102,'Deposit',500.00,'2025-08-11'),
                   (6,103,'withdrawal',100.00,'2025-08-22'),
                   (7,104,'Deposit',500.00,'2025-09-01'),
                   (8,104,'Withdrawal',100.00,'2025-09-10')  ''')

conn.commit()

cursor.close()

conn.close()