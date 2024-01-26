from selenium.webdriver.common.by import By
import pytest, conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_add_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        login_page.fazer_login("standard_user","secret_sauce")

        # mapped aux variables
        add_to_cart_xpath = "//*[text()='ADD TO CART']"
        backpack_product_xpath = "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']"
        continue_shopping_xpath = "//*[text()='Continue Shopping']"
        bike_light_product_xpath = "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']"
        checkout_xpath = "//*[text()='CHECKOUT']"

        # add backpack product to cart
        driver.find_element(By.XPATH, backpack_product_xpath).click()
        driver.find_element(By.XPATH, add_to_cart_xpath).click()
        driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        assert driver.find_element(By.XPATH, backpack_product_xpath).is_displayed()
        driver.find_element(By.XPATH, continue_shopping_xpath).click()

        # add bike light product to cart
        driver.find_element(By.XPATH, bike_light_product_xpath).click()
        driver.find_element(By.XPATH, add_to_cart_xpath).click()
        driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        assert driver.find_element(By.XPATH, bike_light_product_xpath).is_displayed()

        # finish cart
        driver.find_element(By.XPATH, checkout_xpath).click()
        driver.find_element(By.ID, "first-name").send_keys("Rafael")
        driver.find_element(By.ID, "last-name").send_keys("Franca")
        driver.find_element(By.ID, "postal-code").send_keys("1234567")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        driver.find_element(By.XPATH, "//*[text()='FINISH']").click()
        assert driver.find_element(By.CLASS_NAME, "complete-header").text == "THANK YOU FOR YOUR ORDER"
