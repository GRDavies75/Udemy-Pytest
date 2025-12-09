import pytest


@pytest.fixture()
def setup_list() -> list[str]:
    print("\n in fixtures.. \n")
    city = [
        'New York',
        'Londen',
        'Riayadh',
        'Singapore',
        'Mumbai',
    ]

    return city


def test_getItem(setup_list: list[str]) -> None:
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == [
        'New York',
        'Riayadh',
        'Mumbai',
    ]


def myReverse(lst: list[str]) -> list[str]:
    lst.reverse()

    return lst


def test_reverseList(setup_list: list[str]) -> None:
    assert setup_list[::-2] == ['Mumbai', 'Riayadh', 'New York']
    assert setup_list[::-1] == myReverse(setup_list)


@pytest.mark.xfail(reason="Known issue: usefixtures cannot use the fixture's return value")
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo() -> None:
    assert 1 == 1
    print (setup_list[0])
