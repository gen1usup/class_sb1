import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = browser.find_element_by_css_selector('#price')
    # print(browser.find_element_by_css_selector('.card-title').text)
    # print(browser.find_element_by_partial_link_text('Book').text())
    bou_book = browser.find_element_by_id('book')
    # print(browser.find_element_by_partial_link_text('ook').text)
    # print(bou_book.text)
    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    bou_book.click()
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id('solve').click()
    answer = browser.switch_to.alert.text.split(": ")[1]
    print(answer)
    browser.switch_to.alert.accept()

except:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
