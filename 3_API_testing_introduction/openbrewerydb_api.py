import requests

#параметризовать тест
def get_brewery_by_number(number):
    r = requests.get(f"https://api.openbrewerydb.org/breweries/{number}").json()
    return r["id"]
    #print(str(r["id"]) + " get_brewery_by_number - парам тест")

#параметризовать тест
def get_breweries_per_page(per_page):
    params = {"page":1, "per_page":per_page}
    r = requests.get("https://api.openbrewerydb.org/breweries", params=params).json()
    return len(r)
    #print(str(len(r)) + " get_breweries_by_page_per_pag - парам тест")

def get_breweries_by_state(url, state):
    params = {"by_state": state}
    r = requests.get(url, params=params).json()
    return (r[0].get("id"))
    #print(str(r[0].get("id")) + " get_breweries_by_state") #возвращает 4581


def get_breweries_by_tag(url, tag):
    params = {"by_tag": tag}
    r = requests.get(url, params=params).json()
    return len(r)
    #print(str(len(r)) + " get_breweries_by_tag")

def get_breweries_by_name(url, name):
    params = {"by_name": name}
    r = requests.get(url, params=params).json()
    return len(r)
    #print(str(len(r)) + " get_breweries_by_name")




get_brewery_by_number(44)
get_breweries_per_page(10)
get_breweries_by_name("https://api.openbrewerydb.org/breweries", "cooper")
get_breweries_by_tag("https://api.openbrewerydb.org/breweries", "patio")
get_breweries_by_state("https://api.openbrewerydb.org/breweries", "new_york")