import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.label_error_login = (By.XPATH, "//*[@data-test='error']")
        self.msg_erro_esperada_login = "Epic sadface: Username and password do not match any user in this service"

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verificar_msg_erro_login_existe(self):
        self.existe_na_tela(self.label_error_login)

    def verificar_msg_erro_login(self):
        msg_encontrada = self.pegar_texto_elemento(self.label_error_login)
        assert msg_encontrada == self.msg_erro_esperada_login, f"Mensagem encontrada {msg_encontrada} e mensagem esperada {self.msg_erro_esperada_login}"
