import pytest   


@pytest.mark.sanity
def test_str01() -> None:
    num = 9/4
    s1 = 'I like ' + 'pytest automation'
    assert str(num) == '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'


@pytest.mark.sanity
def test_str02() -> None:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26


@pytest.mark.sanity
@pytest.mark.str
def test_str03() -> None:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]


def test_strslice() -> None:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[10:] == 'klmnopqrstuvwxyz'
    assert letters[-3:] == 'xyz'
    assert letters[:21:5] == 'afkpu'


@pytest.mark.str
def test_strsplit() -> None:
    s1 = 'Python,Pytest and Automation'
    assert s1.split() == ['Python,Pytest', 'and', 'Automation']
    assert s1.split(',') == ['Python', 'Pytest and Automation']


#task TBD
def test_strjoin() -> None:
    pass
    s1 = 'Python,Pytest and Automation'
    l1 = ['Python,Pytest', 'and', 'Automation']
    l2 = ['Python', 'Pytest and Automation']
