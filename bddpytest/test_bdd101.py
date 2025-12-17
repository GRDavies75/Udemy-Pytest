from pathlib import Path

import pytest
from pytest_bdd import scenario, given, when, then


FEATURE_FILE_DIR = 'myfeatures' 
FEATURE_FILE_NAME = 'first101.feature' 
BASE_DIR = Path(__file__).parent
FEATURE_FILE = BASE_DIR / FEATURE_FILE_DIR / FEATURE_FILE_NAME


def pytest_configure(): #global variable
    pytest.AMT = 0 # type: ignore


@scenario(FEATURE_FILE, 'Withdrawal of money') # type: ignore
def test_withdrawal():
    print("End of Withdrawal test")
    pass


@given('The account balance is 100')
def current_balance():
    pytest.AMT = 100 # type: ignore


@when('The account holder withdraws 30')
def withdraw_amount():
    pytest.AMT = pytest.AMT - 30 # type: ignore


@then('The account balance should be 70')
def final_balance():
    pytest.AMT == 70 # type: ignore
