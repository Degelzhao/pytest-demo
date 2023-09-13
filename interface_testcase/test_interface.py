import pytest

class TestInterface:
    @pytest.mark.interface
    def test_interface_01(self):
        print("小接口")

if __name__ == "__main__":
    pytest.main(["-s"])