import requests


def test_status_code(url_param):
    status_code = requests.get(url_param).status_code
    assert status_code == 200


