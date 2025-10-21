from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

webdriver_path = r'C:\Users\Иван\Desktop\Репозит\new\chromedriver.exe'
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(2)

    blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")

    blue_button.click()
    time.sleep(2)
    print("Синяя кнопка успешно нажата!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()