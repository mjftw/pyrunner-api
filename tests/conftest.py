import pytest

from pyrunner_api.api import server
from pyrunner_api.runner.pyrunner import PyRunner


@pytest.fixture
def client():
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        yield client


@pytest.fixture
def pyrunner():
    return PyRunner()
