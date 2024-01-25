from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
driver.implicitly_wait(10)

# mapped aux variables
add_to_cart_xpath = "//*[text()='ADD TO CART']"
backpack_product_xpath = "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']"
continue_shopping_xpath = "//*[text()='Continue Shopping']"
bike_light_product_xpath = "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']"
checkout_xpath = "//*[text()='CHECKOUT']"

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# if logged
assert driver.find_element(By.CLASS_NAME, "product_label").is_displayed(), "Login não efetuado!"

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
