from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_hiden = browser.find_element(By.ID, "treasure")
    x_element = x_hiden.get_attribute("valuex")
    x = x_element
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()
    checkbox2 = browser.find_element(By.ID, "robotsRule")
    checkbox2.click()
    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()












