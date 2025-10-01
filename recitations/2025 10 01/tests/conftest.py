# tests/conftest.py
import pytest
from bank_app.account import Account
from bank_app.bank import Bank


# -----------------------
# Common Fixtures
# -----------------------

@pytest.fixture
def valid_account_number():
    """
    Returns a valid account number that passes validate_account_number().
    Adjust this if your validation logic changes.
    """
    return "1004"


@pytest.fixture
def invalid_account_number():
    """
    Returns a definitely invalid account number (non-numeric or wrong length).
    """
    return "invalid123"


@pytest.fixture
def account(valid_account_number):
    """
    Creates a single Account instance with a starting balance of 100.0.
    Used for testing Account directly.
    """
    return Account(
        account_number=valid_account_number,
        account_holder="Alice",
        balance=100.0
    )


@pytest.fixture
def bank():
    """
    Provides a fresh Bank instance for tests that need it.
    """
    return Bank()


@pytest.fixture
def created_account(bank, valid_account_number):
    """
    Creates a Bank instance and adds a valid account to it.
    Used for Bank tests that require an existing account.
    """
    bank.create_account(valid_account_number, "Alice")
    return bank
