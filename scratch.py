from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(2)

x_element = browser.find_element(By.ID, "treasure")
x_element.get_attribute("valuex")
valuex = x_element

x = x_element.get_attribute("valuex")
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = str(calc(x))
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

time.sleep(2)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

checkbox = browser.find_element(By.ID, "robotsRule")
checkbox.click()

submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
submit.click()

time.sleep(5)