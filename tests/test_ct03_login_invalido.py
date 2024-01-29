import pytest
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_inválido(self):
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "zzzzzzzz")
        login_page.verificar_msg_erro_login_existe()
        login_page.verificar_msg_erro_login()