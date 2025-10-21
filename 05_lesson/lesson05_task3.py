from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time


service = FirefoxService(executable_path=GeckoDriverManager().install())


driver = webdriver.Firefox(service=service)


driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, "input")


input_field.send_keys("Sky")
time.sleep(2)


input_field.clear()
time.sleep(2)


input_field.send_keys("Pro")
time.sleep(2)

driver.quit()
