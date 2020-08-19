from flask.app import Flask
import pytest
from pyrunner_api.api import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        yield client


def test_server_should_respond_to_root_request(client):
    response = client.get('/')
    assert response.data
