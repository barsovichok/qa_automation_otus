import pytest


@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture()
def random_dog_url():
    return 'https://dog.ceo/api/breeds/image/random'

@pytest.fixture()
def dog_breed():
    breed = "hound"
    return breed

@pytest.fixture()
def dog_breed_image():
    breed = "hound"
    number = 5
    return breed, number

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