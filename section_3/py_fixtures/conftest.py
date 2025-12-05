from typing import Generator, Any
import os

import pytest

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']
filename = 'file1.txt'


def pytest_configure() -> None:
    pytest.weekdays1 = weekdays1 # type: ignore
    pytest.weekdays2 = weekdays2 # type: ignore


@pytest.fixture(scope="module")
def setup01() -> Generator[list[str], Any, None]:
    wk1 = pytest.weekdays1.copy() # type: ignore

    wk1.append('thur')
    yield wk1
    print("\n After yield in setup01 Fixture")
    # wk1.clear()
    # wk1.pop()


@pytest.fixture
def setup02() -> Generator[list[str], Any, None]:
    wk2 = pytest.weekdays2.copy() # type: ignore
    wk2.insert(0, 'thur')
    yield wk2


@pytest.fixture
def setup03():
    '''
    No type annotation because of Pytest gives problems
    (i cannot resolve at the moment)
    '''
    f = open(filename, 'w')
    f.write("Pytest is good")
    f.close()
    f = open(filename, 'r+')
    yield f
    f.close()
    os.remove(filename)

@pytest.fixture()
def setup04(request):
    print("\n in Fixture setup04")
    print("\n Fixture Scope: " + str(request.scope))
    print("\n Calling function: " + str(request.scope))
