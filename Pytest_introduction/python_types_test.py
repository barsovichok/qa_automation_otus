

from python_types import dictionaries_get, sets, add_set, sum_integers, lists_count, strings_concat, lists_append, list_dicts, strings_len, tuples


class TestPythonExamples:

    def test_integers(self, sum_integers_data):
        assert sum_integers(*sum_integers_data) == 9

    def test_lists_count(self, list_count_data):
        assert lists_count(*list_count_data) == 3

    def test_lists_append(self, lists_append_data):
        assert lists_append(lists_append_data) is True

    def test_strings_concat(self, strings_concat_data):
        assert strings_concat(*strings_concat_data) == "Кот по имени Питон"

    def test_strings_len(self, strings_len_data):
        assert strings_len(strings_len_data) == 10

    def test_dictionaries_get(self, dictionaries_get_data):
        assert dictionaries_get(*dictionaries_get_data) == 24

    def test_list_dicts(self, list_dicts_data):
        assert list_dicts(*list_dicts_data) == {'name': 'iPhone Xs Plus',
                         'stock': 24,
                         'price': 65432.1,
                         'recommended':
                             ['Samsung Galaxy S10',
                              'iPhone Xs']}

    def test_tuples(self, tuples_data):
        assert tuples(tuples_data) == "34fish"

    def test_sets(self, sets_data):
        assert sets(*sets_data) == False

    def test_add_set(self, add_set_data):
        assert add_set(add_set_data) == {'sugar', 'lemon', 'ice', 1}