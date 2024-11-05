from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
knopka = browser.find_element(By.ID, "book")
knopka.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = str(calc(x))
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

knopochka = browser.find_element(By.ID, "solve")
knopochka.click()


time.sleep(6)


