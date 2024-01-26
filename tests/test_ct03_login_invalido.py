from selenium.webdriver.common.by import By
import pytest, conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_inválido(self):
        driver = conftest.driver

        login_page = LoginPage()
        login_page.fazer_login("standard_user","zzzzzzzz")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("zzzzzz")
        driver.find_element(By.ID, "login-button").click()

        # if not logged
        assert driver.find_element(By.XPATH, "//*[@data-test='error']").is_displayed()
