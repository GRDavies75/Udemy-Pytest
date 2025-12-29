import pytest


QA_CONFIG = 'qa.prop'
PROD_CONFIG = 'prod.prop'

def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption('--cmdopt', default='QA')


@pytest.fixture()
def  cmd_opt(pytestconfig: pytest.Config):
    opt = pytestconfig.getoption("cmdopt")
    if opt == 'PROD':
        f = open(PROD_CONFIG, 'r')
    else:
        f = open(QA_CONFIG, 'r')

    yield f
