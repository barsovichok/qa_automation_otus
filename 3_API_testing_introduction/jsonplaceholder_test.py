from jsonplaceholder import get_users, get_posts, get_posts_by_id, get_posts_by_user_id, get_comments_by_post_id

class TestJsonplaceholder:
    def test_get_users(self, get_users_data):
        assert get_users(get_users_data) == 10

    def test_get_posts(self, get_posts_data):
        assert get_posts(get_posts_data) == 100

    def test_get_comments_by_post_id(self, get_comments_by_post_id_data):
        assert get_comments_by_post_id(*get_comments_by_post_id_data) == "Presley.Mueller@myrl.com"

