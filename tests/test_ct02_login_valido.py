import pytest
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_ct02_login_valido(self):
        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("standard_user","secret_sauce")
        home_page.verificar_login_com_sucesso()