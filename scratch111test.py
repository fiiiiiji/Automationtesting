from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

buttonfake = browser.find_element(By.CLASS_NAME, "trollface")
buttonfake.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = str(calc(x))
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

knopochka = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
knopochka.click()


time.sleep(7)