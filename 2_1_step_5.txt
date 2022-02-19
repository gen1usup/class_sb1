from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id("input_value")
x = int(x_element.text)
y = calc(x)

browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_xpath('//label[@for="robotsRule"]').click()
browser.find_element_by_css_selector(".container .btn")
