import pytest


FAHRENHEIT_TO_CELSIUS_RATIO = 9/5
FAHRENHEIT_TO_CELSIUS_OFFSET = 32

def celsius_to_fahrenheit(celc: float = 0.0) -> float:
    fahrenheit = (celc * FAHRENHEIT_TO_CELSIUS_RATIO) + FAHRENHEIT_TO_CELSIUS_OFFSET
    return fahrenheit

# print (celsius_to_fahrenheit())


@pytest.mark.skip(reason="Skipping for no reason specified")
def test_case01() -> None:
    assert type(FAHRENHEIT_TO_CELSIUS_RATIO) == float


def test_case02() -> None:
    assert celsius_to_fahrenheit() == 32

def test_case03() -> None:
    assert celsius_to_fahrenheit(38) == 100.4
