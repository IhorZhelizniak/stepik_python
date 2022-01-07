from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_button = browser.find_element(By.XPATH, '//button[@type ="submit"]')
    find_button.click()

    new_window = browser.window_handles[1]
    current_window = browser.current_window_handle

    browser.switch_to.window(new_window)

    input_value = browser.find_element(By.ID, 'input_value')
    x = input_value.text
    y = calc(x)

    input_field = browser.find_element(By.XPATH, '//input[@id ="answer"]')
    input_field.send_keys(y)

    submit = browser.find_element(By.XPATH, '//button[@type ="submit"]')
    submit.click()

finally:
    time.sleep(30)
    browser.quit()


