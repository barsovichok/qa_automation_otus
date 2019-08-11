from dogceo_api import random_dog_json, random_dog_status,     random_dog_headers,     random_dog_list_sub_breeds_status, random_dog_breeds_image



class TestDogCEOAPI:

    def test_random_dog_json(self, random_dog_url):
        assert random_dog_json(random_dog_url) == 'success'

    def test_random_dog_status(self, random_dog_url):
        assert random_dog_status(random_dog_url) == 200

    def test_random_dog_headers(self, random_dog_url):
        assert random_dog_headers(random_dog_url) == 'application/json'

#Параметриованные тесты - переписать!

    def test_random_dog_list_sub_breeds_status(self, dog_breed):
        assert random_dog_list_sub_breeds_status(dog_breed) == "success"

    def test_random_dog_breeds_image(self, dog_breed_image):
        assert random_dog_breeds_image(*dog_breed_image)[-4:] == '.jpg'

