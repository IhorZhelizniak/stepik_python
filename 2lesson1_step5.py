from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    checkbox1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox1.click()
    checkbox2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    checkbox2.click()
    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()












