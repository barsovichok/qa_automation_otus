from selenium import webdriver
import pytest


def test_stаrt_driver(start_driver, opencart_url):
    """
    Проверяем, что в каждом браузере открывается страница
    :param url_param:
    :return:
    """
    start_driver.get(opencart_url)
    assert start_driver.title == 'Your Store'
    start_driver.close()

