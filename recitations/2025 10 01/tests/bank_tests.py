import pytest
from bank_app.bank import Bank
from bank_app.errors import (
    DuplicateAccountError,
    AccountDoesNotExistError,
    InvalidAccountNumber,
    InsufficientFundsError,
)


# --- Tests for create_account ---
def test_create_account_valid(bank, valid_account_number, capsys):
    bank.create_account(valid_account_number, "Alice")
    assert valid_account_number in bank.accounts
    assert bank.customers["Alice"] == valid_account_number
    captured = capsys.readouterr()
    assert "Created account for Alice" in captured.out


def test_create_account_invalid_number(bank, invalid_account_number):
    with pytest.raises(InvalidAccountNumber) as exc:
        bank.create_account(invalid_account_number, "Bob")
    assert "is not valid" in str(exc.value)


def test_create_account_duplicate(bank, valid_account_number):
    bank.create_account(valid_account_number, "Alice")
    with pytest.raises(DuplicateAccountError) as exc:
        bank.create_account(valid_account_number, "AliceAgain")
    assert "already exists" in str(exc.value)


# --- Tests for deposit ---
def test_deposit_valid(created_account, valid_account_number):
    created_account.deposit(valid_account_number, 50)
    assert created_account.accounts[valid_account_number].balance == 50.0


def test_deposit_invalid_account_number(created_account, invalid_account_number):
    with pytest.raises(InvalidAccountNumber) as exc:
        created_account.deposit(invalid_account_number, 50)
    assert "is not valid" in str(exc.value)


@pytest.mark.parametrize("bad_amount", ["abc", None, [], {}])
def test_deposit_invalid_type(created_account, valid_account_number, bad_amount):
    with pytest.raises(TypeError) as exc:
        created_account.deposit(valid_account_number, bad_amount)
    assert "needs to be a number" in str(exc.value)


def test_deposit_nonexistent_account(bank, valid_account_number):
    # Account is valid format but not created yet
    with pytest.raises(AccountDoesNotExistError) as exc:
        bank.deposit(valid_account_number, 50)
    assert "does not exist" in str(exc.value)


# --- Tests for withdraw ---
def test_withdraw_valid(created_account, valid_account_number):
    created_account.deposit(valid_account_number, 100)
    created_account.withdraw(valid_account_number, 50)
    assert created_account.accounts[valid_account_number].balance == 50.0


def test_withdraw_invalid_account_number(created_account, invalid_account_number):
    with pytest.raises(InvalidAccountNumber) as exc:
        created_account.withdraw(invalid_account_number, 50)
    assert "is not valid" in str(exc.value)


@pytest.mark.parametrize("bad_amount", ["abc", None, [], {}])
def test_withdraw_invalid_type(created_account, valid_account_number, bad_amount):
    with pytest.raises(TypeError) as exc:
        created_account.withdraw(valid_account_number, bad_amount)
    assert "needs to be a number" in str(exc.value)


def test_withdraw_insufficient_funds(created_account, valid_account_number):
    with pytest.raises(InsufficientFundsError) as exc:
        created_account.withdraw(valid_account_number, 200)
    assert "is greater than" in str(exc.value)


# --- Tests for display_account ---
def test_display_account_valid(created_account, valid_account_number, capsys):
    created_account.display_account(valid_account_number)
    captured = capsys.readouterr()
    assert "Account:" in captured.out
    assert "Alice" in captured.out


def test_display_account_invalid_number(created_account, invalid_account_number):
    with pytest.raises(InvalidAccountNumber) as exc:
        created_account.display_account(invalid_account_number)
    assert "is not valid" in str(exc.value)


def test_display_account_nonexistent(bank, valid_account_number):
    with pytest.raises(AccountDoesNotExistError) as exc:
        bank.display_account(valid_account_number)
    assert "does not exist" in str(exc.value)


# --- Tests for get_account_balance ---
def test_get_account_balance_valid(created_account, valid_account_number):
    balance = created_account.get_account_balance(valid_account_number)
    assert balance == 0.0


def test_get_account_balance_invalid_number(created_account, invalid_account_number):
    with pytest.raises(InvalidAccountNumber) as exc:
        created_account.get_account_balance(invalid_account_number)
    assert "is not valid" in str(exc.value)


def test_get_account_balance_nonexistent(bank, valid_account_number):
    with pytest.raises(AccountDoesNotExistError) as exc:
        bank.get_account_balance(valid_account_number)
    assert "does not exist" in str(exc.value)
