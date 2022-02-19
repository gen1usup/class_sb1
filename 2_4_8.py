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
    # browser.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    # browser.find_element_by_xpath('//input[@name="file"]').send_keys('E:\\class_sb1\\2_1_step_5.txt')
    # browser.get("https://stepik.org/lesson/181384/step/8?unit=156009")
    # browser.find_element_by_css_selector('.quiz-component.ember-view').send_keys(answer)



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
