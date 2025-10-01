from bank_app.account import Account
from bank_app.bank import Bank

if __name__ == "__main__":
    bank = Bank()
    
    # Creating accounts
    bank.create_account(1001, "Alice")
    bank.create_account(1002, "Bob")
    
    # Performing some transactions
    bank.deposit(1001, 500)
    # bank.deposit(1001, '500')
    bank.withdraw(1001, 200)
    
    bank.deposit(1002, 1000)
    # bank.withdraw(1002, 1200)  # This will make the balance negative (no validation)

    # Display accounts
    bank.display_account(1001)
    bank.display_account(1002)
    
    # Check balances
    print("Alice's Balance:", bank.get_account_balance(1001))
    print("Bob's Balance:", bank.get_account_balance(1002))