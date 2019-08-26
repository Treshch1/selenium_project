import pytest
from fixtures.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.wd.quit)
    return fixture
