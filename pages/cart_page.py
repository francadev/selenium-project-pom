from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.link_carrinho = (By.CLASS_NAME, 'shopping_cart_link')
        self.item_carrinho = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.continue_shopping = (By.XPATH, "//*[text()='Continue Shopping']")

    def verificar_produto_carrinho(self, nome_item):
        item = (self.item_carrinho[0], self.item_carrinho[1].format(nome_item))
        self.clicar(self.link_carrinho)
        self.existe_na_tela(item)

    def voltar_para_home(self):
        self.clicar(self.continue_shopping)
