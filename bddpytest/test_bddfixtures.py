from pathlib import Path

import pytest
from pytest_bdd import scenarios, given, when, then


FEATURE_FILE_DIR = 'myfeatures' 
FEATURE_FILE_NAME = 'fixtures.feature' 
BASE_DIR = Path(__file__).parent
FEATURE_FILE = BASE_DIR / FEATURE_FILE_DIR / FEATURE_FILE_NAME


def pytest_configure(): #global variable
    # pytest.AMT = 0 # type: ignore
    pass


scenarios(FEATURE_FILE) # type: ignore


@pytest.fixture() # default scope
def setup_set() -> set[str]:
    print("\n In fixture... setup() function... \n")
    countries = {'Poland', 'America', 'Israel', 'Germany', 'Canada'}

    return countries


@given('A datatype set')
def check_set_type(setup_set) -> None:
    print("In Background checking set type")
    if not isinstance(setup_set, set):
        pytest.xfail("The type is not set type")


@given('The set is not empty')
def check_set_notempty(setup_set: set[str]) -> set[str]:
    print("In Background checking set is not empty")
    if len(setup_set) == 0:
        pytest.xfail("The set of elements is empty")
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()

    return setup_set # type: ignore


# # @scenario(FEATURE_FILE, 'Adding to a Set') # type: ignore
# def test_adding_items_to_a_set() -> None:
#     pass


@given('A set with 3 elements', target_fixture='setup_set')
def set_of_elements(setup_set: set[str]) -> set[str]:
    if len(setup_set) == 0:
        pytest.xfail("The set of elements is empty")
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()

    return setup_set # type: ignore


@when('We add 2 elements to the set')
def add_elements(setup_set: set[str]) -> None:
    setup_set.add("India")
    setup_set.add("UK")


@then('The set should have 5 elements')
def final_set_elements(setup_set: set[str]) -> None:
    assert len(setup_set) == 5


# @scenario(FEATURE_FILE, 'Removal of items from set') # type: ignore
# def test_removal_of_item_from_set() -> None:
#     pass


@given('A set of 3 fruits', target_fixture='my_set')
def curent_set() -> set[str]:
    my_set = {"apple", "banana", "cherry"}

    return my_set


@when('We remove a fruit from the set')
def remove_fruit(my_set: set[str]) -> None:
    my_set.pop()
    print(my_set)


@then('The set will have 2 fruits')
def final_set(my_set: set[str]) -> None:
    assert len(my_set) == 2
