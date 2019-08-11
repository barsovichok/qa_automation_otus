import pytest
from openbrewerydb_api import get_brewery_by_number, get_breweries_per_page, get_breweries_by_name, get_breweries_by_tag, get_breweries_by_state


class TestOpenBreweryDBAPI:

    def test_get_breweries_by_name(self, get_breweries_by_name_data):
        """
        Проверяем, что баров с именем Купер и вправду 16
        :param get_breweries_by_name_data:
        :return:
        """
        assert get_breweries_by_name(*get_breweries_by_name_data) == 16

    def test_get_breweries_by_tag(self, get_breweries_by_tag_data):
        """
        Проверяем, чтобаров патио и правда 1. Что это вообще за бар патио? =)
        :param get_breweries_by_tag_data:
        :return:
        """
        assert get_breweries_by_tag(*get_breweries_by_tag_data) == 1

    def test_get_breweries_by_state(self, get_breweries_by_state_data):
        """А это проверка айдишка - гарантия, что каждый раз возращается именно этот бар первый по штату New_york"""
        assert get_breweries_by_state(*get_breweries_by_state_data) == 4581




@pytest.mark.parametrize("test_input, expected", [(8, 8), (6, 6), (42, 42)])
def test_get_brewery_by_number(test_input, expected):
    """Параметризованная роверка ID"""
    assert eval(str(get_brewery_by_number(test_input))) == expected

@pytest.mark.parametrize("test_input, expected", [(9, 9), (50, 50), (25, 25)])
def test_get_breweries_per_page(test_input, expected):
    """Параметризованная проверка ID"""
    assert eval(str(get_breweries_per_page(test_input))) == expected


