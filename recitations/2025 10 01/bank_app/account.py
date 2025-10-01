from bank_app.errors import InsufficientFundsError

class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError('needs to be a number')

        self.balance += amount
        print(f"Deposited {amount} to {self.account_holder}'s account.")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError('needs to be a number')

        if amount > self.balance:
            raise InsufficientFundsError(f'{amount} is greater than {self.balance}')

        self.balance -= amount
        print(f"Withdrew {amount} from {self.account_holder}'s account.")

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"Account: {self.account_number}, Holder: {self.account_holder}, Balance: {self.balance}")