import pytest
from welcom import test_integers


class TestPythonExamples:

    def test_integers(self):
        assert test_integers(4, 5) == 9
