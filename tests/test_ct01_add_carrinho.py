import conftest
import pytest
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import time


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.saucedemo
class TestCT01:
    def test_ct01_add_carrinho(self):
        # pom objects
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        checkout_page = CheckoutPage()

        # products
        product01 = "Sauce Labs Backpack"
        product02 = "Sauce Labs Bike Light"

        # do login
        login_page.fazer_login("standard_user", "secret_sauce")

        # check backpack
        home_page.adicionar_ao_carrinho(product01)
        cart_page.verificar_produto_carrinho(product01)

        # back to home page
        cart_page.voltar_para_home()

        # check bike light
        home_page.adicionar_ao_carrinho(product02)
        cart_page.verificar_produto_carrinho(product02)

        # checkout and finish
        checkout_page.preencher_infos_checkout()
        checkout_page.finalizar_carrinho_e_verificar_se_sucesso()
        
