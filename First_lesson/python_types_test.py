import pytest
from python_types import test_integers, test_lists_count, test_strings_concat, test_lists_append


class TestPythonExamples:

    def test_integers(self):
        assert test_integers(4, 5) == 9

    def test_lists_count(self):
        assert test_lists_count([4, 5, 'i'], [10, "f", "f", "9"]) == 3

    def test_lists_append(self):
        assert test_lists_append([4, 5, 'i']) == [4, 5, 'i', 'Лапка']

