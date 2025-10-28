from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
images = driver.find_elements(By.TAG_NAME, "img")
for image in images:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//img[@src='{image.get_attribute('src')}']")))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//img[@src='{image.get_attribute('src')}']")))

third_image = driver.find_elements(By.TAG_NAME, "img")[2]  
src_attribute = third_image.get_attribute("src")
print(src_attribute)
driver.quit()
