from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
button = driver.find_element(By.ID, "ajaxButton")
button.click()
try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "content"))
    )

    text = element.text

    print(text)

except Exception as e:
    print("Элемент не появился в течение заданного времени.")
    print(e)

finally:
    driver.quit()
