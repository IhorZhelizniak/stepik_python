from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//div[@class ="form-group"]/*[@name ="firstname"]')
    input2 = browser.find_element(By.XPATH, '//div[@class ="form-group"]/*[@name ="lastname"]')
    input3 = browser.find_element(By.XPATH, '//div[@class ="form-group"]/*[@name ="email"]')
    input1.send_keys("Ihor")
    input2.send_keys("Rohi")
    input3.send_keys("bibigul@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    filesend = browser.find_element(By.ID, "file")
    filesend.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

