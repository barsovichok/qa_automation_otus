import requests


def get_brewery_by_number(number):
    """
    Вычисляем бар по айди
    :param number:
    :return:
    """
    r = requests.get(f"https://api.openbrewerydb.org/breweries/{number}").json()
    return r["id"]

def get_breweries_per_page(per_page):
    """
    Тут решаем, сколько баров отобразить на странице
    :param per_page:
    :return:
    """
    params = {"page":1, "per_page":per_page}
    r = requests.get("https://api.openbrewerydb.org/breweries", params=params).json()
    return len(r)

def get_breweries_by_state(url, state):
    """
    Фильтр баров по штату
    :param url:
    :param state:
    :return:
    """
    params = {"by_state": state}
    r = requests.get(url, params=params).json()
    return (r[0].get("id"))


def get_breweries_by_tag(url, tag):
    """
    Фильтр баров по тегу
    :param url:
    :param tag:
    :return:
    """
    params = {"by_tag": tag}
    r = requests.get(url, params=params).json()
    return len(r)

def get_breweries_by_name(url, name):
    """
    Фильтр баров по имени
    :param url:
    :param name:
    :return:
    """
    params = {"by_name": name}
    r = requests.get(url, params=params).json()
    return len(r)


get_brewery_by_number(44)
get_breweries_per_page(10)
get_breweries_by_name("https://api.openbrewerydb.org/breweries", "cooper")
get_breweries_by_tag("https://api.openbrewerydb.org/breweries", "patio")
get_breweries_by_state("https://api.openbrewerydb.org/breweries", "new_york")