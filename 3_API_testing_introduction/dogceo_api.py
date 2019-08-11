import requests


def random_dog_json(url):
    r = requests.get(url).json().get("status")
    return r


def random_dog_status(url):
    return requests.get(url).status_code


def random_dog_headers(url):
    return requests.get(url).headers['Content-Type']


def random_dog_list_sub_breeds_status(breed):
    return requests.get(f'https://dog.ceo/api/breed/{breed}/list').json()['status']


def random_dog_breeds_image(breed, number):
    return requests.get(f'https://dog.ceo/api/breed/{breed}/images/random/{number}').json()['message'][0]


random_dog_json('https://dog.ceo/api/breeds/image/random')
random_dog_status('https://dog.ceo/api/breeds/image/random')
random_dog_headers('https://dog.ceo/api/breeds/image/random')
random_dog_list_sub_breeds_status("hound")
random_dog_breeds_image("hound", 5)


