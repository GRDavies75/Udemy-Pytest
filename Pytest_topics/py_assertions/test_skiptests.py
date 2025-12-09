import pytest


FAHRENHEIT_TO_CELSIUS_RATIO = 9/5
FAHRENHEIT_TO_CELSIUS_OFFSET = 32

def celsius_to_fahrenheit(celcius: float = 0.0) -> float:
    fahrenheit = (celcius * FAHRENHEIT_TO_CELSIUS_RATIO) + FAHRENHEIT_TO_CELSIUS_OFFSET
    return fahrenheit


# print (celsius_to_fahrenheit())


@pytest.mark.skip(reason="Skipping for no reason specified")
def test_case01() -> None:
    assert type(FAHRENHEIT_TO_CELSIUS_RATIO) == float


# @pytest.mark.skipif(sys.version_info > (3,8), reason="Does not work on python version above 3.8")
@pytest.mark.skipif(celsius_to_fahrenheit() == 32, reason="Default value test, so skipping")
def test_case02() -> None:
    assert celsius_to_fahrenheit() == 32


@pytest.mark.skipif(pytest.__version__ > '5.5.0', reason="pytest version is greater then 5.5.0")
def test_case03() -> None:
    assert celsius_to_fahrenheit(38) == 100.4
