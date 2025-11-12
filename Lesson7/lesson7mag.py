import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
  def __init__(self, driver):
    self.driver = driver
    self.username_field = (By.ID, "user-name")
    self.password_field = (By.ID, "password")
    self.login_button = (By.ID, "login-button")

def open(self, url):
  self.driver.get(url)


def enter_username(self, username):
  self.driver.find_element(*self.username_field).send_keys(username)


def enter_password(self, password):
  self.driver.find_element(*self.password_field).send_keys(password)


def click_login(self):
  self.driver.find_element(*self.login_button).click()


class InventoryPage:
  def __init__(self, driver):
    self.driver = driver
    self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    self.bolt_tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    self.onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
    self.cart_link = (By.CLASS_NAME, "shopping_cart_link")


def add_backpack_to_cart(self):
  self.driver.find_element(*self.backpack_add_button).click()


def add_tshirt_to_cart(self):
  self.driver.find_element(*self.bolt_tshirt_add_button).click()


def add_onesie_to_cart(self):
  self.driver.find_element(*self.onesie_add_button).click()


def go_to_cart(self):
  self.driver.find_element(*self.cart_link).click()


class CartPage:
  def __init__(self, driver):
    self.driver = driver
    self.checkout_button = (By.ID, "checkout")


def click_checkout(self):
  self.driver.find_element(*self.checkout_button).click()


class CheckoutPage:
  def __init__(self, driver):
    self.driver = driver
    self.first_name_field = (By.ID, "first-name")
    self.last_name_field = (By.ID, "last-name")
    self.postal_code_field = (By.ID, "postal-code")
    self.continue_button = (By.ID, "continue")
    self.total_label = (By.XPATH, "//div[contains(text(),'Total: $')]")


def enter_information(self, first_name, last_name, postal_code):
  self.driver.find_element(*self.first_name_field).send_keys(first_name)
  self.driver.find_element(*self.last_name_field).send_keys(last_name)
  self.driver.find_element(*self.postal_code_field).send_keys(postal_code)
  self.driver.find_element(*self.continue_button).click()
def get_total(self):
  total_string = self.driver.find_element(*self.total_label).text
  return float(total_string.split('$')[1])


class SauceDemoTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.login_page = LoginPage(self.driver)
    self.inventory_page = InventoryPage(self.driver)
    self.cart_page = CartPage(self.driver)
    self.checkout_page = CheckoutPage(self.driver)


def tearDown(self):
  self.driver.quit()


def test_buy_items(self):
  self.login_page.open("https://www.saucedemo.com/")
  self.login_page.enter_username("standard_user")
  self.login_page.enter_password("secret_sauce")
  self.login_page.click_login()


  self.inventory_page.add_backpack_to_cart()
  self.inventory_page.add_tshirt_to_cart()
  self.inventory_page.add_onesie_to_cart()
  self.inventory_page.go_to_cart()


  self.cart_page.click_checkout()


  self.checkout_page.enter_information("FirstName", "LastName", "12345")
  total_price = self.checkout_page.get_total()
  self.assertEqual(total_price, 58.29)


if __name__ == "__main__":
  unittest.main()
