from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"
link2 = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    findlink = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    findlink.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(30)

    browser.quit()

