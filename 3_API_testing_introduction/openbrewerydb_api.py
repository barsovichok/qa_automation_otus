import requests


def get_brewery_by_number(url, number):
    r = requests.get(f"{url}{number}").json()
    #return r["id"]
    print(r["id"])

def get_breweries_by_page_per_page(url, page, per_page):
    params = {"page":page, "per_page":per_page}
    r = requests.get(url, params=params).json()
    #return len(r)
    print(len(r))

def get_breweries_by_state(url, state):
    params = {"by_state":state}
    r = requests.get(url, params=params).json()
    #return len(r)
    print(len(r))

def get_breweries_by_tag(url,tag):
    params = {"by_tag":tag}
    r = requests.get(url, params=params).json()
    #return len(r)
    print(len(r))

def get_breweries_by_name(url, name):
    params = {"by_name":name}
    r = requests.get(url, params=params).json()
    #return len(r)
    print(len(r))



get_brewery_by_number('https://api.openbrewerydb.org/breweries/', 44)
get_breweries_by_page_per_page("https://api.openbrewerydb.org/breweries", 2, 10)
get_breweries_by_name("https://api.openbrewerydb.org/breweries", "cooper")
get_breweries_by_tag("https://api.openbrewerydb.org/breweries", "patio")
get_breweries_by_state("https://api.openbrewerydb.org/breweries", "new_york")