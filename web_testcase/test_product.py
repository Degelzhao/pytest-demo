import time

import pytest

class TestLogin:
    @pytest.mark.product
    def test_product_01(self):
        time.sleep(3)
        print("小趴菜")

if __name__ == "__main__":
    pytest.main(["-s"])