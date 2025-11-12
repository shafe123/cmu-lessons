import pytest
from bank_app.errors import InsufficientFundsError, InvalidAccountNumber
from bank_app.account import Account


# --- Tests for __init__ ---
def test_init_valid_account(account, valid_account_number):
    assert account.account_number == valid_account_number
    assert account.account_holder == "Alice"
    assert account.balance == 100.0


def test_init_invalid_account_number(invalid_account_number):
    # Invalid account number should raise InvalidAccountNumber
    with pytest.raises(InvalidAccountNumber) as exc:
        Account(account_number=invalid_account_number,
                account_holder="Bob",
                balance=50.0)
    assert "is not valid" in str(exc.value)


def test_init_zero_or_negative_balance(valid_account_number):
    with pytest.raises(ValueError) as exc:
        Account(account_number=valid_account_number,
                account_holder="Charlie",
                balance=0)
    assert "Initial balance cannot be negative" in str(exc.value)


# --- Tests for deposit ---
def test_deposit_valid(account, capsys):
    account.deposit(50.0)
    assert account.balance == 150.0
    captured = capsys.readouterr()
    assert "Deposited 50.0" in captured.out


@pytest.mark.parametrize("bad_value", ["abc", None, [], {}])
def test_deposit_invalid_type(account, bad_value):
    with pytest.raises(TypeError) as exc:
        account.deposit(bad_value)
    assert "needs to be a number" in str(exc.value)


@pytest.mark.parametrize("bad_amount", [0, -10])
def test_deposit_non_positive(account, bad_amount):
    with pytest.raises(ValueError) as exc:
        account.deposit(bad_amount)
    assert "Deposit cannot be negative" in str(exc.value)


# --- Tests for withdraw ---
def test_withdraw_valid(account, capsys):
    account.withdraw(50.0)
    assert account.balance == 50.0
    captured = capsys.readouterr()
    assert "Withdrew 50.0" in captured.out


@pytest.mark.parametrize("bad_value", ["abc", None, [], {}])
def test_withdraw_invalid_type(account, bad_value):
    with pytest.raises(TypeError) as exc:
        account.withdraw(bad_value)
    assert "needs to be a number" in str(exc.value)


@pytest.mark.parametrize("bad_amount", [0, -20])
def test_withdraw_non_positive(account, bad_amount):
    with pytest.raises(ValueError) as exc:
        account.withdraw(bad_amount)
    assert "Withdrawal cannot be negative" in str(exc.value)


def test_withdraw_insufficient_funds(account):
    with pytest.raises(InsufficientFundsError) as exc:
        account.withdraw(200.0)
    assert "is greater than" in str(exc.value)


# --- Tests for get_balance ---
def test_get_balance(account):
    assert account.get_balance() == 100.0


# --- Tests for display ---
def test_display(account, capsys):
    account.display()
    captured = capsys.readouterr()
    assert f"Account: {account.account_number}" in captured.out
    assert f"Holder: {account.account_holder}" in captured.out
    assert f"Balance: {account.balance}" in captured.out
