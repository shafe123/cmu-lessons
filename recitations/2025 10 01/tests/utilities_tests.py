import pytest
from bank_app.utilities import validate_account_number

def test_account_valid(valid_account_number):
    assert validate_account_number(valid_account_number)

def test_account_invalid(invalid_account_number):
    assert not validate_account_number(invalid_account_number)