import json


def test_server_should_respond_to_root_request(client):
    response = client.get('/')
    assert response.data


def test_server_run_python_should_respond_status_200_to_post(client):
    code = '#'
    response = client.post('/run/python', data='')
    assert 200 == response.status_code


def test_server_run_python_should_respond_with_json_data(client):
    response = client.post('/run/python', data='')

    # Check no json.decoder.JSONDecodeError is raised
    json.loads(response.data)


def test_server_run_python_should_have_stdout_in_data(client):
    response = client.post('/run/python', data='')

    assert 'stdout' in json.loads(response.data)


def test_server_run_python_should_have_stderr_in_data(client):
    response = client.post('/run/python', data='')

    assert 'stderr' in json.loads(response.data)


def test_server_run_python_should_return_python_stdout(client):
    response = client.post('/run/python', data='print("Hello World!")')

    assert 'Hello World!\n' == json.loads(response.data).get('stdout')
