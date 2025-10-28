from selenium import webdriver
from selenium.webdriver.common.by import By

def rename_button():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    updated_button_text = button.text
    print(updated_button_text)
    driver.quit()

rename_button()
