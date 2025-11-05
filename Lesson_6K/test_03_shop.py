import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout_flow():

    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items_to_add:
        add_button_locator = (By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button")
        driver.find_element(*add_button_locator).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Имя")
    driver.find_element(By.ID, "last-name").send_keys("Фамилия")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    total_locator = (By.XPATH, "//div[@class='summary_info_label' and text()='Total: ']/following-sibling::div[@class='summary_info_label']")
    total = driver.find_element(*total_locator).text

    assert total == "$58.29", f"Итоговая сумма не совпадает: {total}"

    driver.quit()
