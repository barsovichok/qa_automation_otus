from openbrewerydb_api import get_brewery_by_number, get_breweries_by_page_per_page, get_breweries_by_name, get_breweries_by_tag, get_breweries_by_state


class TestOpenBreweryDBAPI:

    def test_get_breweries_by_name(self, get_breweries_by_name_data):
        assert get_breweries_by_name(*get_breweries_by_name_data) == 16

    def test_get_breweries_by_tag(self, get_breweries_by_tag_data):
        assert get_breweries_by_tag(*get_breweries_by_tag_data) == 1

    def test_get_breweries_by_state(self, get_breweries_by_state_data):
        assert get_breweries_by_state(*get_breweries_by_state_data) == 4581


