from typing import Generator

import pytest


weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']

@pytest.fixture()
def setup01() -> Generator[list[str]]:
    wk1 = weekdays1.copy()
    wk1.append('thur')
    yield wk1
    print("\n After yield in setup01 Fixture")
    # wk1.clear()
    wk1.pop()


def test_extendList(setup01) -> None:
    setup01.extend(weekdays2)
    assert setup01 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
