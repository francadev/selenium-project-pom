import conftest
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def fazer_login(self, usuario, senha):
        driver = conftest.driver
        driver.find_element(*self.username_field).send_keys(usuario)
        driver.find_element(*self.password_field).send_keys(senha)
        driver.find_element(*self.login_button).click()
