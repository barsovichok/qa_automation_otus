from dogceo_api import random_dog_json, random_dog_status, random_dog_headers
from dogceo_api import random_dog_list_sub_breeds_status, random_dog_breeds_image



class TestDogCEOAPI:
    """Это класс с тестовыми функциями, которые не параметризованы"""
    def test_random_dog_json(self, random_dog_url):
        """Эта тестовая функция проверяет значение поля status в пришедшем от API json-e"""
        assert random_dog_json(random_dog_url) == 'success'

    def test_random_dog_status(self, random_dog_url):
        """Эта тестовая функция проверяет, что ответ пришёл со статусом 200"""
        assert random_dog_status(random_dog_url) == 200

    def test_random_dog_headers(self, random_dog_url):
        """
        та тестовая функция проверяет, что ответ от сервера пришёл в формате json
        :param random_dog_url:
        :return:
        """
        assert random_dog_headers(random_dog_url) == 'application/json'

    def test_random_dog_list_sub_breeds_status(self, dog_breed):
        """
        Эта тестовая функция проверяет значение поля status в пришедшем от API json-e
        :param dog_breed:
        :return:
        """
        assert random_dog_list_sub_breeds_status(dog_breed) == "success"

    def test_random_dog_breeds_image(self, dog_breed_image):
        """
               Эта тестовая функция проверяет, что в ответе от сайта пришла картинка (формат jpg, jpeg)
               :param dog_breed:
               :return:
               """
        random_dog_breeds_image_1 = (random_dog_breeds_image(*dog_breed_image)[-4:]).lower()
        if random_dog_breeds_image_1 == '.jpeg':
            random_dog_breeds_image_1 = '.jpg'
            assert random_dog_breeds_image_1 == '.jpg'
        else:
            assert (random_dog_breeds_image(*dog_breed_image)[-4:]).lower() == '.jpg'

