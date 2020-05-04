import pytest
from .initiate_driver import *

@pytest.fixture(scope="module")
def test_setup_teardown():
    url = "https://www.goibibo.com/"
    driver.maximize_window()
    driver.get(url)
    yield
    driver.close()

