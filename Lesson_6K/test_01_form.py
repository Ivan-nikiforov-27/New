import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(params=["edge", "safari"])
def driver(request):
    if request.param == "edge":
        driver = webdriver.Edge()
    elif request.param == "safari":
        driver = webdriver.Safari()
    yield driver
    driver.quit()

def test_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    
    driver.find_element(By.NAME, "firstName").send_keys("Иван")
    driver.find_element(By.NAME, "lastName").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phoneNumber").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "jobTitle").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary").click()

    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".is-invalid, .is-valid")))

    
    zip_code = driver.find_element(By.NAME, "zipCode")
    assert "is-invalid" in zip_code.get_attribute("class"), "Zip code не красный"

    
    fields = ["firstName", "lastName", "address", "email", "phoneNumber", "city", "country", "jobTitle", "company"]
    for field in fields:
        element = driver.find_element(By.NAME, field)
        assert "is-valid" in element.get_attribute("class"), f"{field} не зеленый"
