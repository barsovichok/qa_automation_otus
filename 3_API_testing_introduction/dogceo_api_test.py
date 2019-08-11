import pytest

from dogceo_api import random_dog_json


class TestPythonExamples:
    def test_random_dog_json(self):
        assert random_dog_json('https://dog.ceo/api/breeds/image/random') == 'success'
