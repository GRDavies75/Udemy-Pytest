from pathlib import Path

import pytest
from pytest_bdd import scenarios, given, when, then, parsers


FEATURE_FILE_DIR = 'myfeatures' 
FEATURE_FILE_NAME = 'parameterize.feature' 
BASE_DIR = Path(__file__).parent
FEATURE_FILE = BASE_DIR / FEATURE_FILE_DIR / FEATURE_FILE_NAME


scenarios(FEATURE_FILE) # type: ignore


@given('There are 3 varieties of fruits', target_fixture='fruits')
def existing_fruits() -> set[str]:
    fruits = {'apples', 'grapes', 'strawberries'}

    return fruits


@when('We add a same variety of fruit')
def add_a_fruit(fruits) -> None:
    fruits.add("grapes")


@then('There is same count of varieties')
def same_count(fruits) -> None:
    assert len(fruits) == 3


@then('If we add a different variety of fruit')
def add_diff_variety(fruits) -> None:
    fruits.add("cherry")


@then(parsers.parse('The count of varieties increases to {count:d}'))
def count_increases(fruits, count) -> None:
    assert len(fruits) == count
