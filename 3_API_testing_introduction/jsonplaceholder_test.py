import pytest
from jsonplaceholder import get_users, get_posts, get_posts_by_id, get_posts_by_user_id, get_comments_by_post_id

class TestJsonplaceholder:
    def test_get_users(self, get_users_data):
        """Тестовая функция, которая проверяет, что пользователей у нас 10.
        Если пользователей станет больше, то тест обвалится"""
        assert get_users(get_users_data) == 10

    def test_get_posts(self, get_posts_data):
        """
        естовая функция, которая проверяет, что постов у нас 100.
        Если пользователей станет больше, то тест обвалится
        """
        assert get_posts(get_posts_data) == 100

    def test_get_comments_by_post_id(self, get_comments_by_post_id_data):
        """Проверяем, что коммент оставил именно этот имейл, и сюда слать гневные письма"""
        assert get_comments_by_post_id(*get_comments_by_post_id_data) == "Presley.Mueller@myrl.com"

    def test_get_posts_by_user_id(self, get_posts_by_user_id_data):
        """
        Тут что-то сложное, я забыла, в чём прикол.
        Кажется, что title точно приходит в ответе мы здесь проверяем
        :param get_posts_by_user_id_data:
        :return:
        """
        assert str(get_posts_by_user_id(*get_posts_by_user_id_data)) == "<class 'int'>"


@pytest.mark.parametrize("post_id", [1, 5, 7, 9, 8, 6, 4, 3, 2, 42])
def test_get_posts_by_id(post_id):
    """
    Тут всё просто, проверяем по айди, что пришёл именно тот пост
    :param post_id:
    :return:
    """
    assert get_posts_by_id(post_id) == post_id

