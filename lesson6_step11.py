from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # link1 - success
    # link2 - failure

    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    # Поменять переменную в browser.get(link)
    browser.get(link2)

    input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[(@class="form-group first_class")]/input[@class="form-control first"]')
    input1.send_keys("Ihor")

    input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[(@class="form-group second_class")]/input[@class="form-control second"]')
    input2.send_keys("Zhel")

    input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[(@class="form-group third_class")]/input[@class="form-control third"]')
    input3.send_keys("bibigul@gmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)

    browser.quit()

