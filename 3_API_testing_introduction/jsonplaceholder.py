import requests


def get_users(url):
    r = requests.get(url).json()
    return len(r)


def get_posts(url):
    r = requests.get(url).json()
    """Функция отдаёт все опбуликованные посты почему-то"""
    return len(r)



def get_posts_by_id(post_id):
    r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}").json()
    """Функция возвращает пост по айди, но кому это нужно"""
    return r.get("id")



def get_posts_by_user_id(user_id, user_title):
    """
    О, а это функция, которая проверяет, что в ответе от сайта есть значение title (а я хочу спать)
    :param user_id:
    :param user_title:
    :return:
    """
    params = {"user_id": user_id}
    r = requests.get("https://jsonplaceholder.typicode.com/posts", params=params).json()
    return type(list(r[user_title].keys()).index("title"))



def get_comments_by_post_id(url, post_id, post_email):
    """Эта классная функция возвращает email комментатора, чтобы забросать его гневными письмами в случае чего"""
    params = {"post_id": post_id}
    r = requests.get(url, params=params).json()
    return r[post_email].get("email")



get_users("https://jsonplaceholder.typicode.com/users")
get_posts("https://jsonplaceholder.typicode.com/posts")
get_comments_by_post_id("https://jsonplaceholder.typicode.com/comments", 1, 5)
get_posts_by_user_id(1, 5)
get_posts_by_id(1)
