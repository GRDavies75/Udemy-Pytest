'''
Parameterization with fixtures
'''
import pytest


@pytest.fixture(params=[(3,4),[3,5]],ids=['tuple','list'])
def fixture01(request: pytest.FixtureRequest):
    return request.param
    

@pytest.fixture(params=["access", "slice", "assign", "len"])
def fixture02(request: pytest.FixtureRequest):
    return request.param


def test_fixture_param01(fixture01) -> None:
    assert (type(fixture01)) in [tuple, list]


def test_fixture_param02(fixture01, fixture02) -> None:
    if fixture02 == "access":
        assert fixture01[0]
    elif fixture02 == "slice":
        assert fixture01[::-1]
    elif fixture02 == "len":
        assert len(fixture01)
