import os
import time

from selenium.webdriver.support.ui import Select

from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    # browser.maximize_window()
    # time.sleep(5)
    browser.get(link)
    browser.find_element_by_css_selector('.trollface.btn').click()
    browser.switch_to.window(browser.window_handles[1])
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    # browser.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    # browser.find_element_by_xpath('//input[@name="file"]').send_keys('E:\\class_sb1\\2_1_step_5.txt')

    #
    # x_element = browser.find_element_by_id("input_value")
    # x = int(x_element.text)
    # y = calc(x)
    # browser.find_element_by_id("answer").send_keys(y)
    # browser.find_element_by_id('robotCheckbox').click()
    # radiobutton = browser.find_element_by_xpath('//label[@for="robotsRule"]')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    # radiobutton.click()
    # button = browser.find_element_by_class_name("container .btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))

except:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
