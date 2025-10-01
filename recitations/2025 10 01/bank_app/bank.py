from bank_app.account import Account


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        account = Account(account_number, account_holder)
        self.accounts[account_number] = account
        self.customers[account_holder] = account_number
        print(f"Created account for {account_holder}.")

    def deposit(self, account_number, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("needs to be a number")

        account = self.accounts[account_number]
        account.deposit(amount)

    def withdraw(self, account_number, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("needs to be a number")

        account = self.accounts[account_number]
        account.withdraw(amount)

    def display_account(self, account_number):
        account = self.accounts[account_number]
        account.display()

    def get_account_balance(self, account_number):
        account = self.accounts[account_number]
        return account.get_balance()
