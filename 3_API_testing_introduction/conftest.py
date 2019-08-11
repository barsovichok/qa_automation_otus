import pytest


@pytest.fixture()
def random_dog_url():
    return 'https://dog.ceo/api/breeds/image/random'


@pytest.fixture(params=["akita", "bulldog", "collie", "dalmatian", "dingo", "mastiff", "mix"])
def dog_breed(request):
    return request.param


@pytest.fixture(params=[("akita", 1), ("bulldog", 4), ("collie", 5), ("dalmatian", 5), ("dingo", 9), ("mastiff", 1), ("mix", 1)])
def dog_breed_image(request):
    return request.param


@pytest.fixture(scope="function", params=[(1, 10), (2, 5), (6, 3), (12, 6)])
def get_posts_by_user_id_data(request):
    return request.param


@pytest.fixture()
def get_users_data():
    return "https://jsonplaceholder.typicode.com/users"

@pytest.fixture()
def get_posts_data():
    return "https://jsonplaceholder.typicode.com/posts"

@pytest.fixture()
def get_comments_by_post_id_data():
    return "https://jsonplaceholder.typicode.com/comments", 1, 5


@pytest.fixture()
def get_breweries_by_name_data():
    return "https://api.openbrewerydb.org/breweries", "cooper"


@pytest.fixture()
def get_breweries_by_tag_data():
    return "https://api.openbrewerydb.org/breweries", "patio"


@pytest.fixture()
def get_breweries_by_state_data():
    return "https://api.openbrewerydb.org/breweries", "new_york"


@pytest.fixture(params = [1, 10, 42, 56, 89, 23, 5])
def get_breweries_by_page_per_page_data(request):
    return request.param

