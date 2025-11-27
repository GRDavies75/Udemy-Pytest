import pytest

import math


@pytest.mark.parametrize('test_input', [82, 78, 55, 66])
def test_param01(test_input: int)-> None:
    assert test_input > 50


@pytest.mark.parametrize('input, output', [(2,4), (3,27), (4,256)])
def test_param02(input: int, output: int)-> None:
    assert (input ** input) == output


data = [
    ([2,3,4], 'sum', 9),
    ([2,3,4], 'prod', 24),
]

@pytest.mark.parametrize("a,b,c", data)
def test_param03(a: list[int], b: str, c: int):
    if b == 'sum':
        assert sum(a) == c
    elif b == 'prod':
        assert math.prod(a) == c
