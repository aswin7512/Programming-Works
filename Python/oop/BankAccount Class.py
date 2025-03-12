#class_BankAccount
class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.owner_name = name
        self.acc_no = acc_no
        self.balance = balance
    
    
    def deposit(self, amt):
        self.balance += amt
        print(f"Rs.{amt} DEPOSITED SUCCESSFULLY...")
    
    
    def withdraw(self, amt):
        self.balance -= amt
        print(f"Rs.{amt} WITHDRAWN SUCCESSFULLY...")
    
    
    def check_balance(self):
        return self.balance


usr1 = BankAccount(name = input("ENTER YOUR NAME: "),
                   acc_no = int(input("ENTER YOUR ACCOUNT NUMBER: ")),
                   balance = float(input("ENTER YOUR CURRENT BALANCE: ")))

usr1.withdraw(amt = float(input("ENTER AMOUNT TO WITHDRAW: ")))

usr1.deposit(amt = float(input("ENTER AMOUNT TO DEPOSIT: ")))

print(usr1.check_balance())