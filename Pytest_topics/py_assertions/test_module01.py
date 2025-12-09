
def test_a1() -> None:
    assert 4 != 3


def test_a2() -> None:
    assert 1


# test no.3
def test_a3() -> None:
    assert "abcd" == 'abcd'


def test_a4() -> None:
    assert ((3-1)*4/2) == 4.0


def test_a5() -> None:
    assert 1 in divmod(9,5)
    assert 'py' in 'this is pytest'
