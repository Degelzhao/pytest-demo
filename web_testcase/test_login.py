import time

import pytest


class TestLogin1:
    def test_login_01(self):
        print("小菜鸡01")

    def test_login_02(self):
        print("小菜鸡02")

    def test_login_03(self):
        print("小菜鸡03")

    def test_login_04(self):
        print("小菜鸡04")

class TestLogin2:
    def test_login_01(self):
        print("小菜鸟01")

    def test_login_02(self):
        print("小菜鸟02")



if __name__ == "__main__":
    pytest.main(["-s"])