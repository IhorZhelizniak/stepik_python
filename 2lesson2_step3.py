from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    numfind1 = browser.find_element(By.ID, "num1")
    numfind2 = browser.find_element(By.ID, "num2")

    num1 = numfind1.text
    num2 = numfind2.text

    answer = int(num1) + int(num2)

    select1 = Select(browser.find_element(By.TAG_NAME, "select"))
    select1.select_by_value(str(answer))

    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()