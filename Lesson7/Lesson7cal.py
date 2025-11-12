import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
   def __init__(self, driver: WebDriver):
     self.driver = driver
     self.delay_input = (By.ID, "delay")
     self.seven_button = (By.XPATH, "//span[text()='7']")
     self.plus_button = (By.XPATH, "//span[text()='+']")
     self.eight_button = (By.XPATH, "//span[text()='8']")
     self.equals_button = (By.XPATH, "//span[text()='=']")
     self.result_field = (By.ID, "result")
def open(self, url):
     self.driver.get(url)


def enter_delay(self, delay):
   delay_element = self.driver.find_element(*self.delay_input)
   delay_element.send_keys(delay)


def press_button(self, button_locator):
   button = self.driver.find_element(*button_locator)
   button.click()


def get_result(self):
  
  WebDriverWait(self.driver, 50).until(  
  EC.text_to_be_present_in_element(self.result_field, "15"))
  result_element = self.driver.find_element(*self.result_field)
  return result_element.text


class CalculatorTest(unittest.TestCase):
   def setUp(self):
      self.driver = webdriver.Chrome()
      self.page = CalculatorPage(self.driver)


def tearDown(self):
   self.driver.quit()

def test_calculator(self):
   self.page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
   self.page.enter_delay("45")
   self.page.press_button(self.page.seven_button)
   self.page.press_button(self.page.plus_button)
   self.page.press_button(self.page.eight_button)
   self.page.press_button(self.page.equals_button)
   result = self.page.get_result()
   self.assertEqual(result, "15")


if __name__ == "__main__":
   unittest.main()