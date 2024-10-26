import pytest

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_login(self):
        print("demo")