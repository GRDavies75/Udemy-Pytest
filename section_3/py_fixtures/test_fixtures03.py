from typing import Generator, Any

import pytest


def test_delItem(setup01: list[str]) -> None:
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekdays1 # type: ignore


def test_removeItem(setup02: list[str]) -> None:
    print(setup02)
    setup02.remove('thur')
    assert setup02 == pytest.weekdays2 # type: ignore
