import requests


def random_dog_json(url):
    r = requests.get(url)
    r = r.json()
    r = r.keys()
    return r
    #print(r.json())


def random_dog_status():
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    return r.status_code
    #print(r.status_code)


def random_dog_headers():
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    return r.headers['Content-Type']
  #  print(r.headers['Content-Type'])


def random_dog_list_sub_breeds_status(breed):
    r = requests.get(f'https://dog.ceo/api/breed/{breed}/list')
    r = r.json()
    return r['status']
   # print(r['status'])

def random_dog_breeds_number(number):
    r = requests.get(f'https://dog.ceo/api/breed/hound/images/random/{number}')
    r = r.json()
    message_list = r['message']
    return len(message_list)
    #print(len(message_list))


random_dog_json('https://dog.ceo/api/breeds/image/random')
random_dog_status()
random_dog_headers()
random_dog_list_sub_breeds_status("hound")
random_dog_breeds_number(5)


