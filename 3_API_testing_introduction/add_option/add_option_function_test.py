import requests


def test_status_code(url_param):
    """
    Проверяем входящий параметр (урл) на код статуса - должен быть 200
    :param url_param:
    :return:
    """
    status_code = requests.get(url_param).status_code
    assert status_code == 200


