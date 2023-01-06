import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input_value = browser.find_element(By.ID, 'input_value').text
    input_math = math.log(abs(12*math.sin(int(input_value))))
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(str(input_math))
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

time.sleep(15)
