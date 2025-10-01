from bank_app.account import Account
from bank_app.errors import (
    DuplicateAccountError,
    AccountDoesNotExistError,
    InvalidAccountNumber,
)


def validate_account_number(number):
    return len(str(number)) == 4


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if not validate_account_number(account_number):
            raise InvalidAccountNumber(f"{account_number} is not valid")

        if account_number in self.accounts:
            raise DuplicateAccountError(f"{account_number} already exists")

        account = Account(account_number, account_holder)
        self.accounts[account_number] = account
        self.customers[account_holder] = account_number
        print(f"Created account for {account_holder}.")

    def deposit(self, account_number, amount):
        if not validate_account_number(account_number):
            raise InvalidAccountNumber(f"{account_number} is not valid")

        if not isinstance(amount, (int, float)):
            raise TypeError("needs to be a number")

        if account_number not in self.accounts:
            raise AccountDoesNotExistError(
                f"{account_number} does not exist at this bank"
            )

        account = self.accounts[account_number]
        account.deposit(amount)

    def withdraw(self, account_number, amount):
        if not validate_account_number(account_number):
            raise InvalidAccountNumber(f"{account_number} is not valid")

        if not isinstance(amount, (int, float)):
            raise TypeError("needs to be a number")

        account = self.accounts[account_number]
        account.withdraw(amount)

    def display_account(self, account_number):
        if not validate_account_number(account_number):
            raise InvalidAccountNumber(f"{account_number} is not valid")

        if account_number not in self.accounts:
            raise AccountDoesNotExistError(
                f"{account_number} does not exist at this bank"
            )

        account = self.accounts[account_number]
        account.display()

    def get_account_balance(self, account_number):
        if not validate_account_number(account_number):
            raise InvalidAccountNumber(f"{account_number} is not valid")

        if account_number not in self.accounts:
            raise AccountDoesNotExistError(
                f"{account_number} does not exist at this bank"
            )

        account = self.accounts[account_number]
        return account.get_balance()
