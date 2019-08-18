from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="ie",
        help="This is request browser",
        required=True
    )

@pytest.fixture
def browser_param(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def start_driver(browser_param):
    if browser_param == "chrome":
        driver = webdriver.Chrome("C:\Tools\chromedriver.exe")
        return driver
        # driver.get("http://www.python.org")
        # assert "Python" in driver.title
        # driver.close()
    elif browser_param == "firefox":
        driver = webdriver.Chrome("C:\Tools\geckodriver.exe")
        return driver
        # driver.get("http://www.python.org")
        # assert "Python" in driver.title
        # driver.close()
    #request.addFinalizer(wd.quit)
    #return wd