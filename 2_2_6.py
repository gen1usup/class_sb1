import time

from selenium.webdriver.support.ui import Select

from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    # time.sleep(5)
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    radiobutton = browser.find_element_by_xpath('//label[@for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element_by_class_name("container .btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

except:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
