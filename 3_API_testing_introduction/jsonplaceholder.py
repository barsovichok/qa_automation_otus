import requests


def get_users(url):
    r = requests.get(url).json()
    #return len(r) - 10
    return len(r)


def get_posts(url):
    r = requests.get(url).json()
    #return len(r) - 100
    return len(r)


#параметризовать тест
def get_posts_by_id(url, post_id):
    r = requests.get(f"{url}{post_id}").json()
    return r.get("id")

#параметризовать тест
def get_posts_by_user_id(url, user_id, user_title):
    params = {"user_id": user_id}
    r = requests.get(url, params=params).json()
    return type(list(r[user_title].keys()).index("title"))



def get_comments_by_post_id(url, post_id, post_email):
    params = {"post_id": post_id}
    r = requests.get(url, params=params).json()
    return r[post_email].get("email")
    #Presley.Mueller@myrl.com


get_users("https://jsonplaceholder.typicode.com/users")
get_posts("https://jsonplaceholder.typicode.com/posts")
get_comments_by_post_id("https://jsonplaceholder.typicode.com/comments", 1, 5)
get_posts_by_user_id("https://jsonplaceholder.typicode.com/posts", 1, 5) #параметризовать тест
get_posts_by_id("https://jsonplaceholder.typicode.com/posts/", 1) #параметризовать тест
