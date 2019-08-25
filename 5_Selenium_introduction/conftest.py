from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="ie",
        help="This is request browser",
        required=False
    )

    parser.addoption(
        "--opencart_url",
        action="store",
        default="http://localhost/OpencartStore/",
        help="This is opencart_url",
        required=False
    )



@pytest.fixture()
def browser_param(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def opencart_url_param(request):
    return request.config.getoption("--opencart_url")


@pytest.fixture()
def start_driver(browser_param):
    if browser_param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        return driver
    elif browser_param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        return driver
    elif browser_param == "ie":
        options = webdriver.IeOptions()
        options.add_argument("--headless")
        driver = webdriver.Ie(options=options)
        return driver


@pytest.fixture()
def opencart_url(opencart_url_param):
    return opencart_url_param
