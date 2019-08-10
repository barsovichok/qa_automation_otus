import requests

def get_users(url):
    r = requests.get(url).json()
    #return r["id"]
    print(len(r))

def get_posts(url):
    r = requests.get(url).json()
    #return r["id"]
    print(len(r))

get_users("https://jsonplaceholder.typicode.com/users")
get_posts("https://jsonplaceholder.typicode.com/posts")
/posts/1/comments