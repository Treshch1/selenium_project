import pytest
from fixtures.application import Application

fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
