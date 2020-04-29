import pytest
from browser_initiator import driver

@pytest.fixture(scope='module')
def setup_teardown():
    url = 'https://www.selenium.dev/'
    driver.maximize_window()
    driver.get(url)