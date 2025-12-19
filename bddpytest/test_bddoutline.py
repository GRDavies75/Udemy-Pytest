from pathlib import Path

import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers


FEATURE_FILE_DIR = 'myfeatures' 
FEATURE_FILE_NAME = 'scenariooutline.feature' 
BASE_DIR: Path = Path(__file__).parent
FEATURE_FILE: Path = BASE_DIR / FEATURE_FILE_DIR / FEATURE_FILE_NAME


# scenarios(FEATURE_FILE) # type: ignore

@scenario(FEATURE_FILE, 'Scene Outline Test') # type: ignore
def test_outline() -> None:
    pass


@given(parsers.parse('There are {start: d} cucumbers'), target_fixture='cucumbers')
def existing_cucumbers(start: int) -> dict[str, int]:
    return dict(start = start)


@when(parsers.parse('I deposit {deposit:d} cucumbers'))
def deposit_cucumbers(cucumbers: dict[str, int], deposit: int) -> None:
    cucumbers['deposit'] = deposit
    print(cucumbers)


@when(parsers.parse('I withdraw {withdraw:d} cucumbers'))
def withdraw_cucumbers(cucumbers: dict[str, int], withdraw: int) -> None:
    cucumbers['withdraw'] = withdraw
    print(cucumbers)


@then(parsers.parse('I should have {final:d} cucumbers'))
def final_cucumbers(cucumbers: dict[str, int], final) -> None:
    assert cucumbers['start'] + cucumbers['deposit'] - cucumbers['withdraw'] == final

# ----------------- End of scenario 1 ------------------
