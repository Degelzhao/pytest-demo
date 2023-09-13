import pytest


@pytest.fixture(scope="function", autouse=True)
def my_fixture():
    print("web前置")
    yield
    print("web后置")