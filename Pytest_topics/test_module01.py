
def test_a1() -> None:
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1


def test_a2() -> None:
    assert 7.5 / 5 == 1.5, "failed test due to poor math"


# test no.3
def test_a3() -> None:
    assert 9 // 5 == 1, "failed test intentionally"
