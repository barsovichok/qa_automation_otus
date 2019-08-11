import pytest


@pytest.fixture()
def random_dog_url():
    """
    Фикстура возвращает урл, по которому отдается рандомная картинка
    :return:
    """
    return 'https://dog.ceo/api/breeds/image/random'


@pytest.fixture(params=["akita", "bulldog", "collie", "dalmatian", "dingo", "mastiff", "mix"])
def dog_breed(request):
    """
    Фикстура возвращает набор тестовых параметров (породы собак)
    :param request:
    :return:
    """
    return request.param


@pytest.fixture(params=[("akita", 1), ("bulldog", 4), ("collie", 5),
                        ("dalmatian", 5), ("dingo", 9), ("mastiff", 1),
                        ("mix", 1)]
                )
def dog_breed_image(request):
    """
        Фикстура возвращает набор тестовых параметров (породы собак и ID картинки)
        :param request:
        :return:
        """
    return request.param


@pytest.fixture(scope="function", params=[(1, 10), (2, 5), (6, 3), (12, 6)])
def get_posts_by_user_id_data(request):
    """
        Фикстура возвращает набор тестовых параметров (первое число - user_id, второе - количетсво постов от юзера)
        :param request:
        :return:
        """
    return request.param


@pytest.fixture()
def get_users_data():
    """
        Фикстура возвращает урл (количество зарегистрированных юзеров)
        :param request:
        :return:
        """
    return "https://jsonplaceholder.typicode.com/users"

@pytest.fixture()
def get_posts_data():
    """
    Фикстура возвращает урл (количество опубликованных постов)
    :return:
    """
    return "https://jsonplaceholder.typicode.com/posts"

@pytest.fixture()
def get_comments_by_post_id_data():
    """
    Фикстура возвращает урл (количество комментов к конкретному посту)
    :return:
    """
    return "https://jsonplaceholder.typicode.com/comments", 1, 5


@pytest.fixture()
def get_breweries_by_name_data():
    """
    Фикстура возвращает урл (количество баров с конкретным именем)
    :return:
    """
    return "https://api.openbrewerydb.org/breweries", "cooper"


@pytest.fixture()
def get_breweries_by_tag_data():
    """
     Фикстура возвращает урл (количество баров с конкретным тэгом)
    :return:
    """
    return "https://api.openbrewerydb.org/breweries", "patio"


@pytest.fixture()
def get_breweries_by_state_data():
    """
     Фикстура возвращает урл (количество баров в конкретном штате)
    :return:
    """
    return "https://api.openbrewerydb.org/breweries", "new_york"



