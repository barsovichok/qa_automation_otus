

from python_types import dictionaries_get, sets, add_set, sum_integers, lists_count, strings_concat, lists_append, list_dicts, strings_len, tuples


class TestPythonExamples:

    def test_integers(sum_integers_data):
        assert sum_integers(sum_integers_data) == 9

    def test_lists_count(self):
        assert lists_count([4, 5, 'i'], [10, "f", "f", "9"]) == 3

    def test_lists_append(self):
        assert lists_append([4, 5, 'i']) is True

    def test_strings_concat(self):
        assert strings_concat(a="Кот ", b="по имени ", c="Питон") == "Кот по имени Питон"

    def test_strings_len(self):
        assert strings_len, ("мармозетка") == 10

    def test_dictionaries_get(self):
        assert dictionaries_get(product={"name": "iPhone Xs", "stock": 24, "price": 65432.1},
                                     key_product="stock") == 24

    def test_list_dicts(self):
        assert list_dicts(stock=[
            {'name': 'iPhone Xs Plus',
             'stock': 24,
             'price': 65432.1,
             'recommended': ['Samsung Galaxy S10', 'iPhone Xs']},
            {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
            {'name': 'Xiaomi Mi8',
             'stock': 42,
             'price': 38000.5
             }
        ], number=0) == {'name': 'iPhone Xs Plus',
                         'stock': 24,
                         'price': 65432.1,
                         'recommended':
                             ['Samsung Galaxy S10',
                              'iPhone Xs']}

    def test_tuples(self):
        assert tuples((1, 3, 4, "fish", 4)) == "34fish"

    def test_sets(self):
        assert sets({'son', 'daddy', 'mum'}, {'sugar', 'lemon', 'ice'}) == False

    def test_add_set(self):
        assert add_set({'sugar', 'lemon', 'ice'}) == {'sugar', 'lemon', 'ice', 1}