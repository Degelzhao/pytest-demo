import pytest

if __name__ == "__main__":
    pytest.main(["-vs", "./web_testcase/test_login.py", "-n=2", "--reruns=2"])