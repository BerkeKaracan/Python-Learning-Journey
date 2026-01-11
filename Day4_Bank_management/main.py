import sqlite3
import time
class Bank :
    def __init__(self):
        self.con = sqlite3.connect('bank.db')
        self.cursor = self.con.cursor()
        query = "CREATE TABLE IF NOT EXISTS  accounts (name TEXT, account_no TEXT, balance REAL, password TEXT)"
        self.cursor.execute(query)
        self.con.commit()

    def create_account(self):
        name = input("Enter your name: ")
        account_no = input("Enter your account number: ")
        password = input("Create a 4-digit PIN code: ")
        self.cursor.execute("SELECT * FROM accounts WHERE account_no = ?", (account_no,))
        existing_accounts = self.cursor.fetchall()
        if len(existing_accounts) > 0 :
            print("Account already exists")

        else:
            insert_query  = "INSERT INTO accounts VALUES (?,?,?,?)"
            self.cursor.execute(insert_query, (name,account_no,0,password))
            self.con.commit()
            print(f"Account created for {name} with 0 Balance.")

    def deposit_money(self):
        print(" -- DEPOSITING MONEY --")
        account_no = input("Enter account number: ")
        self.cursor.execute("SELECT * FROM accounts WHERE account_no = ?", (account_no,))
        account = self.cursor.fetchall()
        if len(account) == 0 :
            print("Account not exists")

        else:
            entered_pass = input("Enter your PIN code: ")
            real_pass = account[0][3]

            if entered_pass != real_pass:
                print(" WRONG PIN! Access Denied.")
                return
            try:
                amount = float(input("Enter amount to deposit: "))
            except ValueError:
                print("Error: Please enter a valid number! (Only numbers)")
                return
            update_query =  "UPDATE accounts SET balance = balance + ? WHERE account_no = ?"
            self.cursor.execute(update_query, (amount, account_no))
            self.con.commit()
            print(f"{amount:.2f} added to account. New Balance updated.")

    def withdraw_money(self):
        print(" -- WITHDRAWAL MONEY --")
        account_no = input("Enter account number: ")
        self.cursor.execute("SELECT * FROM accounts WHERE account_no = ?", (account_no,))
        account = self.cursor.fetchall()
        if len(account) == 0 :
            print("Account not exists")
        else:
            entered_pass = input("Enter your PIN code: ")
            real_pass = account[0][3]

            if entered_pass != real_pass:
                print(" WRONG PIN! Access Denied.")
                return
            try:
                amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("Error: Please enter a valid number! (Only numbers)")
                return
            current_balance = account[0][2]
            if current_balance >= amount:
                update_query = "UPDATE accounts SET balance = balance - ? WHERE account_no = ?"
                self.cursor.execute(update_query, (amount, account_no))
                self.con.commit()
                print(f"Account withdrawal {amount:.2f} Balance.")
            else:
                print(f"Your account doesn't have enough money.")
    def check_balance(self):
        print(" -- CHECK BALANCE --")
        account_no = input("Enter account number: ")
        self.cursor.execute("SELECT * FROM accounts WHERE account_no = ?", (account_no,))
        account = self.cursor.fetchall()
        if len(account) == 0 :
            print("Account not exists")
        else:
            name = account[0][0]
            balance = account[0][2]
            print(f"Name: {name} | Balance: ${balance:.2f}")

bank = Bank()
while True:
    a = input('''
    ******************************
        BANK MANAGEMENT SYSTEM
    ******************************
    1 - Create Account
    2 - Deposit Money
    3 - Withdraw Money
    4 - Check Balance
    Q - Exit
    
    What would you like to do? :: 
    ''').upper()
    if a == "1":
        bank.create_account()
        time.sleep(1.5)
    elif a == "2":
        b = input("ARE YOU SURE ? : (Y/N)").upper()
        if b == "Y" :
            bank.deposit_money()
            time.sleep(1.5)
        else:
            continue
    elif a == "3":
        b = input("ARE YOU SURE ? : (Y/N)").upper()
        if b == "Y" :
            bank.withdraw_money()
            time.sleep(1.5)
        else:
            continue
    elif a == "4":
            bank.check_balance()
            time.sleep(1.5)
    elif a == "Q" :
        print("\nThank you for choosing us. Goodbye! 👋")
        break