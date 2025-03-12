import db

table_name = 'bank_records'

class Person(object):
    def __init__(self, name, username):
        self.name = name
        self.username = username

    def print_person_details(self):
        print(
          f"\nPerson details:\
            \n\t> Name: {self.name}\
            \n\t> Username: {self.username}\n"
        )


class DebitCard(Person):
    card_type = "VISA"

    def __init__(self, pin, name, username):
        self._pin = pin
        Person.__init__(self, name, username)

    def get_pin(self):
        return self._pin

    def print_card_details(self):
        print(
           f"\nDebitCard details:\
            \n\t> Card holder: {self.name}\
            \n\t> PIN: XXXX\
            \n\t> Card type: {self.card_type}"
        )


class BankAccount(DebitCard):
    bank_name = "HDFC"
    branch = "GOA"
    account_type = "CURRENT"

    def __init__(self, username, acc_no, name, pin, balance):
        self.acc_no = acc_no
        self._balance = balance
        DebitCard.__init__(self, pin, name, username)

    def get_balance(self):
        self._balance = db.fetch_balance(table_name, self.username)
        return self._balance

    def deposit(self, amount):
        db.update_balance(table_name,
                          self.acc_no,
                          amount)

        print(f"${amount} has been credited to your account.")
        print(f"Balance is ${self.get_balance()}")

    def withdraw(self, amount):
        if self.get_balance() >= amount:
            amount *= -1
            db.update_balance(table_name,
                                self.acc_no,
                                amount)

            print(f"${amount} is debited.")
            print(f"Your balance is ${self.get_balance()}")
            return True
        else:
            print("Insufficient balance.")
            print(f"Your balance is ${self.get_balance()}")
            return False

    def print_account_details(self):
        print(
                f"### {self.bank_name} Bank, {self.branch} ###\
                \n> Account type: {self.account_type} account\
                \n> Account holder: {self.name}\
                \n> Account number: {self.acc_no}\
                \n> Branch: {self.branch}\
                \n> Bank balance: ${self.get_balance()}"
        )
        self.print_person_details()
        self.print_card_details()

    def print_statement(self):
        print("%4s%20s%20s"%("Sno.","AMOUNT","BALANCE"))
        print()
        statements = db.get_statement(self.acc_no)
        i = 1
        if len(statements) > 10:
            i = len(statements) - 9
            statements = statements[-10: ]
        for item in statements:
            print("%4s%20s%20s"%(i, item[0], item[1]))
            i += 1


    def send_money(self, acc_no, amount):
        if self.withdraw(amount):
            db.update_balance(table_name, acc_no, amount)
            print(f"${amount} has been successfully Sent to Account no. {acc_no}")



def validate_username(uname):
    for i in uname:
        if i.isupper():
            return False
    return True