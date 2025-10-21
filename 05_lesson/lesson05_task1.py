from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def run_test():
    
    driver = webdriver.Chrome()  

    
    driver.get("http://uitestingplayground.com/classattr")

    
    try:
        blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
        blue_button.click()

        
        time.sleep(2)

    except Exception as e:
        print(f"Ошибка при выполнении теста: {e}")

    finally:
        
        driver.quit()


for i in range(1):
    run_test()
    
    

