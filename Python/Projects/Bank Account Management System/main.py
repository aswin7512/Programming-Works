import os
from methords import BankAccount, validate_username
import db


table_name = db.init_table("bank_records")

while True:
    #try:
        os.system('cls')
        choice = int(input("Welcome to HDFC Bank\
                            \n\nEnter a Choice\
                            \n(1) Login to your account\
                            \n(2) Open an account\
                            \n(0) Exit\
                            \n=> "))

        if choice == 2:
            name = input("Enter your name: ")
            username = input("Enter you username: ")
            if not validate_username(username):
                print("Username contains invalid characters\
                \nUsername cannot contain an \"Upper Case\" Character")
                input("Press Enter to Restart!!!")
                continue
            if db.does_uname_exist(table_name, username):
                print(f"Username {username} is already taken.")
                input("Press Enter to Restart!!!")
                continue
            pin = int(input("Enter your Debit card pin: "))
            balance = float(input("Enter an amount to Depsit: "))

            db.create_user(table_name, username, name, pin, balance)

        elif choice == 0:
            db.close_conn()
            break
        elif choice != 1:
            print("Invalid option.")
            input("Press Enter to Restart!!!")
            continue

        os.system('cls')
        print("Please Authenticate...\n")
        username = input("Enter your username: ")
        if not db.does_uname_exist(table_name, username):
            print("Invalid username.")
            input("Press Enter to Restart!!!")
            continue
        pin = int(input("Enter your PIN number: "))
        username, acc_no, name, pin, balance = db.authenticate(table_name, username, pin)

        if username is None:
            print("Invalid PIN number!!!")
            input("Press Enter to Restart")
            continue

        account_buf = BankAccount(username, acc_no, name, pin, float(balance))
        while True:
            os.system('cls')
            acc_control = int(input(
                            f"Welcome {account_buf.name},\
                                \nChoose an operation\
                                \n(1) withdraw\
                                \n(2) deposit\
                                \n(3) check balance\
                                \n(4) view account details\
                                \n(5) statement\
                                \n(6) send money\
                                \n(0) logout\
                                \n=> "
                            ))
            print("\n")
            if acc_control == 1:
                amount = float(input("Enter an amount to withdraw: $"))
                account_buf.withdraw(amount)
            elif acc_control == 2:
                amount = float(input("Enter an amount to deposit: $"))
                account_buf.deposit(amount)
            elif acc_control == 3:
                print(f"Your balance is ${account_buf.get_balance()}")
            elif acc_control == 4:
                account_buf.print_account_details()
            elif acc_control == 5:
                account_buf.print_statement()
            elif acc_control == 6:
                acc_no = int(input("Enter Receiver's Account Number: "))
                name = input("Enter Reciever's name: ")
                if not db.valid_acc_no(table_name, acc_no, name):
                    print("Invalid User: Account Number or Name doesn't match!\n")
                    input("Press Enter To Restart!!!")
                    continue
                amount = float(input("Enter Amount to Send: $"))
                if amount < 1.0:
                    print("Min Transaction Amount is $1")
                    input("Press Enter to Restart!!!")
                    continue
                account_buf.send_money(acc_no, amount)
            elif acc_control == 0:
                break
            else:
                print("Invalid option.")
            input("Press Enter to Continue!!!")
'''except:
        print("SOME ERROR OCCURED\
            \n PLEASE TRY AGAIN!!!")'''