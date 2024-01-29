from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.checkout = (By.XPATH, "//*[text()='CHECKOUT']")
        self.first_name_label = (By.ID, "first-name")
        self.last_name_label = (By.ID, "last-name")
        self.postal_code_label = (By.ID, "postal-code")
        self.continue_label = (By.XPATH, "//input[@type='submit']")
        self.finalizar_carrinho = (By.XPATH, "//*[text()='FINISH']")
        self.pedido_finalizado_com_sucesso_label = (By.CLASS_NAME, "complete-header")
        self.msg_esperada = "THANK YOU FOR YOUR ORDER"

    def preencher_infos_checkout(self):
        self.clicar(self.checkout)
        self.escrever(self.first_name_label, "Rafael")
        self.escrever(self.last_name_label, "Franca")
        self.escrever(self.postal_code_label, "1234567")
        self.clicar(self.continue_label)

    def finalizar_carrinho_e_verificar_se_sucesso(self):
        self.clicar(self.finalizar_carrinho)
        msg_encontrada = self.pegar_texto_elemento(self.pedido_finalizado_com_sucesso_label)
        assert msg_encontrada == self.msg_esperada, f"Mensagem encontrada {msg_encontrada} e mensagem esperada {self.msg_esperada}"
