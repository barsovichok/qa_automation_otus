import pytest


@pytest.fixture()
def sum_integers_data():
    return 4, 5

@pytest.fixture()
def list_count_data():
    return [4, 5, 'i'], [10, "f", "f", "9"]

@pytest.fixture()
def lists_append_data():
    lists_append_data = [4, 5, 'i']
    return lists_append_data


@pytest.fixture()
def strings_concat_data():
    return "Кот ", "по имени ", "Питон"


@pytest.fixture()
def strings_len_data():
    strings_len_data = "мармозетка"
    return strings_len_data


@pytest.fixture()
def dictionaries_get_data():
    return {"name": "iPhone Xs", "stock": 24, "price": 65432.1}, "stock"

@pytest.fixture()
def list_dicts_data():
    return [
            {'name': 'iPhone Xs Plus',
             'stock': 24,
             'price': 65432.1,
             'recommended': ['Samsung Galaxy S10', 'iPhone Xs']},
            {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
            {'name': 'Xiaomi Mi8',
             'stock': 42,
             'price': 38000.5
             }
        ], 0



@pytest.fixture()
def tuples_data():
    return 1, 3, 4, "fish", 4


@pytest.fixture()
def sets_data():
    return {'son', 'daddy', 'mum'}, {'sugar', 'lemon', 'ice'}


@pytest.fixture()
def add_set_data():
    return {'sugar', 'lemon', 'ice'}
