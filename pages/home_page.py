import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.CLASS_NAME, "product_label")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.add_to_cart = (By.XPATH, "//*[text()='ADD TO CART']")

        #self.bike_light_product = (By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']")
        #self.backpack_product = (By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']")

    def verificar_login_com_sucesso(self):
        self.existe_na_tela(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.add_to_cart)
