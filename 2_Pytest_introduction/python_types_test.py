

from python_types import dictionaries_get, sets, add_set, sum_integers, lists_count, strings_concat, lists_append, list_dicts, strings_len, tuples


class TestPythonExamples:

    def test_start_fixtures(self, module_fixture, session_fixture):
        return module_fixture, session_fixture

    def test_integers(self, sum_integers_data):
        """
        Test checks Python data type "integer"
        :param sum_integers_data:
        :return: sum of two integers
        """

        assert sum_integers(*sum_integers_data) == 9

    def test_lists_count(self, list_count_data):
        """
        Test checks Python data type "list"
        :param list_count_data:
        :return: count some data in list
        """
        assert lists_count(*list_count_data) == 3

    def test_lists_append(self, lists_append_data):

        """
        Test checks Python data type "list" (add new data in list)
        :param lists_append_data:
        :return: new data in list
        """
        assert lists_append(lists_append_data) is True

    def test_strings_concat(self, strings_concat_data):
        """
        Test checks Python data type "string"
        :param strings_concat_data:
        :return: concatenate string from seeral strings
        """
        assert strings_concat(*strings_concat_data) == "Кот по имени Питон"

    def test_strings_len(self, strings_len_data):
        """
        Test checks Python data type "string"
        :param strings_len_data:
        :return: integer - string lenght
        """
        assert strings_len(strings_len_data) == 10

    def test_dictionaries_get(self, dictionaries_get_data):
        """
        Test checks Python data type "dictionary"
        :param dictionaries_get_data:
        :return: value by key
        """
        assert dictionaries_get(*dictionaries_get_data) == 24

    def test_list_dicts(self, list_dicts_data):
        """
        Test checks Python data type "dictionary"
        :param list_dicts_data:
        :return: value from  by meaning
        """
        assert list_dicts(*list_dicts_data) == {'name': 'iPhone Xs Plus',
                         'stock': 24,
                         'price': 65432.1,
                         'recommended':
                             ['Samsung Galaxy S10',
                              'iPhone Xs']}

    def test_tuples(self, tuples_data):
        """
        Test checks Python data type "tuple"
        :param tuples_data:
        :return: concatenate string data from tple
        """
        assert tuples(tuples_data) == "34fish"

    def test_sets(self, sets_data):
        """
        Test checks Python type "set"
        :param sets_data:
        :return: boolean False - wrong try to find some common data in two sets
        """
        assert sets(*sets_data) == False

    def test_add_set(self, add_set_data):
        """
        Test checks free addition some data to type set

        :param add_set_data:
        :return: add data to set
        """
        assert add_set(add_set_data) == {'sugar', 'lemon', 'ice', 1}