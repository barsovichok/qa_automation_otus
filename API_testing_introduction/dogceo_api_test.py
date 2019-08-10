import pytest

from dogceo_api import random_dog_json


class TestPythonExamples:
    def random_dog_json(self):
        assert random_dog_json('https://dog.ceo/api/breeds/image/random') == ['message', 'status']
