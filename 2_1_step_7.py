from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
x = int(browser.find_element_by_xpath('//img[@src="images/chest.png"]').get_attribute("valuex"))
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_xpath('//*[@id="robotsRule"]').click()
browser.find_element_by_css_selector(".container .btn")
