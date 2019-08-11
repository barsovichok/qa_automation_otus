import pytest
import argparse

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )



def test_answer(url_param):
    if url_param == "ya.ru":
        print("YAAAAANDEX")
    elif url_param == "google.com":
        print("GOOOGLE!")
    else:
        print("DuckDuckGOOOOO")



