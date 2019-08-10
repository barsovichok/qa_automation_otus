def sum_integers(int1, int2):
    # type: (integer, integer) -> integer
    return int1 + int2


def lists_count(list1, list2):
    # type: (list, list) -> list
    return list1.count(5) + list2.count("f")


def lists_append(list):
    # type: (list) -> bool
    len_list = len(list)
    list.append('Лапка')
    len_new_list = len(list)
    return len_list < len_new_list


def strings_concat(string1, string2, string3):
    # type: (string, string, string) -> string
    return f"{string1}{string2}{string3}"


def strings_len(strings_len):
    # type: (string) -> int
    return len(strings_len)


def dictionaries_get(product, key_product):
    # type: (dict) -> string
    return product.get(key_product)


def list_dicts(stock, number):
    return stock[number]


def tuples(tuple):
    return str(tuple[1]) + str(tuple[2]) + tuple[3]


def sets(set1, set2):
    return set1 in set2


def add_set(add_set):
    add_set.add(1)
    return add_set
