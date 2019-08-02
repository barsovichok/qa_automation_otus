import pytest

from python_types import test_dictionaries_get, test_sets, test_add_sets, test_add_sets, test_integers, test_lists_count, test_strings_concat, test_lists_append, test_list_dicts,test_strings_len, test_tuples


class TestPythonExamples:

    def test_integers(self):
        assert test_integers(4, 5) == 9

    def test_lists_count(self):
        assert test_lists_count([4, 5, 'i'], [10, "f", "f", "9"]) == 3

    def test_lists_append(self):
        assert test_lists_append([4, 5, 'i']) is True

    def test_strings_concat(self):
        assert test_strings_concat(a="Кот ", b="по имени ", c="Питон") == "Кот по имени Питон"

    def test_strings_len(self):
        assert test_strings_len, ("мармозетка") == 10

    def test_dictionaries_get(self):
        assert test_dictionaries_get(product={"name": "iPhone Xs", "stock": 24, "price": 65432.1},
                                     key_product="stock") == 24

    def test_list_dicts(self):
        assert test_list_dicts(stock=[
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
        assert test_tuples((1, 3, 4, "fish", 4)) == "34fish"

    def test_sets(self):
        assert test_sets({'son', 'daddy', 'mum'}, {'sugar', 'lemon', 'ice'}) == False

    def test_add_sets(self):
        assert test_add_sets({'sugar', 'lemon', 'ice'}) == {'sugar', 'lemon', 'ice', 1}