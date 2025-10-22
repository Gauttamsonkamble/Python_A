
import sqlite3 

conn = sqlite3.connect('bank.db')

cursor = conn.cursor()

cursor.execute(''' create table if not exists customers (custId integer primary key, name text not null, address text, email text unique) ''')

cursor.execute(''' create table if not exists Accounts (acc_id integer primary key, custId integer, acc_type text, balance real, foreign key (custId) references key) ''')

cursor.execute(''' create table if not exists Transanction (trans_id integer primary key, acc_id integer, trans_type text, ammount real, date date, foreign key (acc_id) references account) ''')

conn.commit()
cursor.close()

conn.close()