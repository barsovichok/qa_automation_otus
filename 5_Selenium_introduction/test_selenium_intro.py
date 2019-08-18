from selenium import webdriver
import pytest


def test_stаrt_driver(start_driver):
    """
    Проверяем, что в каждом браузере открывается страница
    :param url_param:
    :return:
    """
    start_driver.get("http://www.python.org")
    assert start_driver.title == "Welcome to Python.org"

