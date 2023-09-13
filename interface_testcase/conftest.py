import pytest


@pytest.fixture(scope="class", autouse=True)
def my_fixture():
    print("interface前置")
    yield
    print("interface后置")