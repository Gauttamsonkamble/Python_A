
# List Details of all customers

import sqlite3

def show_customers():
    conn = sqlite3.connect('bank.db')

    cursor = conn.cursor()

    result = cursor.execute("select * from customers")
    for row in result:
        print(row)

    conn.close()



def show_accounts():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    result = cursor.execute(''' select Accounts.acc_id, customers.name, Accounts.acc_type,Accounts.balance from Accounts join customers on Accounts.custId = customers.custId ''')

    for row in result:
        print(row)

    conn.close()


def show_Transanction():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    result = cursor.execute("select * from Transanction")

    for row in result:
        print(row)

    conn.close()

if __name__ == "__main__":
    print("\n\n Customers : ")
    show_customers()

    print("\n\n Accounts : ")
    show_accounts()

    print("\n\n Transanctions : ")
    show_Transanction()