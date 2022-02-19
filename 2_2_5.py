from datetime import time

from selenium.webdriver.support.ui import Select

from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    spisok = Select(browser.find_element_by_tag_name("select"))
    spisok.select_by_value(str(num1 + num2))
    browser.find_element_by_class_name("container .btn").click()
except:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
