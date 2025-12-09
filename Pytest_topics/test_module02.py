
class TestMyStuff():
    def test_type(self) -> None:
        assert type(1.3) == int


    def test_strs(self) -> None:
        assert str.upper('python') == 'PYTHON'
        assert 'pytest'.capitalize() == 'Pytest'
    