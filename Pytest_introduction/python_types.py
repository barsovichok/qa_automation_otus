def sum_integers(a, b):
    # type: (integer, integer) -> integer
    return a+b

def lists_count(a,b):
    # type: (list, list) -> list
    return a.count(5) + b.count("f")


def lists_append(a):
    # type: (list) -> bool
    c = len(a)
    a.append('Лапка')
    b = len(a)
    return c < b


def strings_concat(a,b,c):
    # type: (string, string, string) -> string
    return f"{a}{b}{c}"


def strings_len(a: object) -> object:
    # type: (string) -> int
    return len(a)


def dictionaries_get(product, key_product):
    # type: (dict) -> string
    return product.get(key_product)


def list_dicts(stock, number):
    return stock[number]


def tuples(tuple):
    return str(tuple[1]) + str(tuple[2]) + tuple[3]


def sets(set1, set2):
    return set1 in set2


def add_set(b):
    b.add(1)
    return b

#
# strings_concat = strings_concat(a="Кот ", b="по имени ", c="Питон")
# sum_integers = sum_integers(4, 5)
# lists_append = lists_append(a=[4, 5, 'i'])
# lists_count = lists_count(a=[4, 5, 'i'], b=[10, "f", "f", "9"])
# strings_len = strings_len("мармозетка")
# dictionaries_get= dictionaries_get(product={"name": "iPhone Xs","stock": 24,"price": 65432.1}, key_product="stock")
# list_dicts = list_dicts(stock=[{'name': 'iPhone Xs Plus',
#                             'stock': 24,
#                             'price': 65432.1,
#                             'recommended': ['Samsung Galaxy S10', 'iPhone Xs']},
#                            {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
#                            {'name': 'Xiaomi Mi8',
#                             'stock': 42,
#                             'price': 38000.5}], number=0)
# tuples = tuples(tuple=(1, 3, 4, "fish", 4))
# sets = sets(set1={'son', 'daddy', 'mum'}, set2={'sugar', 'lemon', 'ice'})
# add_set = add_set(b={'sugar', 'lemon', 'ice'})


