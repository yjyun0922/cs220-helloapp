import pytest
import sys, os

p = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, p + '/../')

from hello.main import app as helloapp



@pytest.fixture
def app():
    helloapp.config["TESTING"] = True

    return helloapp

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
