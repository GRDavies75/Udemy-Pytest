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
def add_a_fruit(fruits: set[str]) -> None:
    fruits.add("grapes")


@then('There is same count of varieties')
def same_count(fruits: set[str]) -> None:
    assert len(fruits) == 3


@then('If we add a different variety of fruit')
def add_diff_variety(fruits: set[str]) -> None:
    fruits.add("cherry")


@then(parsers.parse('The count of varieties increases to {count:d}'))
def count_increases(fruits: set[str], count: int) -> None:
    assert len(fruits) == count

# ----------------- End of scenario 1 ------------------

# Global variable
pytest.total_fruits = 0 # type: ignore


@given(parsers.parse('Given there are {count:d} fruits'), target_fixture='start_fruits')
def existing_dict_of_fruits(count: int) -> dict[str, int]:
    pytest.total_fruits = count # type: ignore

    return dict(start=count, eat=0)


@when(parsers.parse('I eat {eat:d} fruits'))
def eat_fruits(start_fruits, eat) -> None:
    start_fruits["eat"] += eat
    print(start_fruits)


@then(parsers.parse('I should have {left:d} fruits'))
def should_have_left_fruits(start_fruits: dict[str, int], left):
    assert start_fruits['start'] == pytest.total_fruits # type: ignore
    assert start_fruits['start'] - start_fruits['eat'] == left
