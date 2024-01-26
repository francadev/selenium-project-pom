from selenium import webdriver
import pytest
driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/v1/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    # run test
    yield

    # teardown
    driver.quit()
