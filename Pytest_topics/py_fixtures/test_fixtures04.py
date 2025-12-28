import pytest


months = ["Jan", "Feb", "Mar"]


def test_checkrequest(setup04: pytest.FixtureRequest) -> None:
    assert "Apr" in setup04 # type: ignore
    assert len(setup04) == 4 #type: ignore
    

def test_factory_fixture(setup05) -> None:
    assert type(setup05('list')) == list
    assert type(setup05('tuple')) == tuple