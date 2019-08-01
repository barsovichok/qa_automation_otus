def test_integers(a, b):
    # type: (integer, integer) -> integer
    return a + b

def test_lists_count(a,b):
    # type: (list, list) -> list
    return a.count(5) + b.count("f")


def test_lists_append(a):
    # type: (list) -> list
    return a.append('Лапка')


def test_strings_concat(a,b,c):
    # type: (string, string, string) -> string
    return f"{a}{b}{c}"


def test_strings_len(a):
    # type: (string) -> int
    return len(a)


def test_dictionaries_get(product, key_product):
    # type: (dict) -> string
    return product.get(key_product)


def test_list_dicts(stock, number):
    return stock[number]

def test_tuples(tuple):
    return str(tuple[1]) + str(tuple[2]) + tuple[3]


def test_sets(set, other_set):
    return set in other_set


def test_add_sets(b):
    return b.add(1)


if __name__ == "__main__":
    test_strings_concat(a="Кот ", b="по имени ", c="Питон")
    test_integers(4, 5)
    test_lists_append(a=[4, 5, 'i'])
    test_lists_count(a=[4, 5, 'i'], b=[10, "f", "f", "9"])
    test_strings_len("мармозетка")
    test_dictionaries_get(product={"name": "iPhone Xs","stock": 24,"price": 65432.1}, key_product="stock")
    test_list_dicts(stock=[{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'recommended': ['Samsung Galaxy S10', 'iPhone Xs']}, {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000}, {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}], number=0)
    test_tuples(tuple=(1, 3, 4, "fish", 4))
    test_sets(set={'son', 'daddy', 'mum'}, other_set={'sugar', 'lemon', 'ice'})
    test_add_sets(b={'sugar', 'lemon', 'ice'})


