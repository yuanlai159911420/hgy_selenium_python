from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.relative_locator import locate_with

if __name__ == '__main__':
    # url = "http://www.wxt.plus:50037/auth/login"
    url = "http://139.9.244.72:50002/auth/login"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 10)
    username_ele = driver.find_element(By.ID, "username")
    # password_ele = locate_with(By.ID, "password").below(username_ele)
    password_ele = locate_with(By.ID, "password").below({By.ID: "username"})
    driver.find_element(password_ele).send_keys("1234")
