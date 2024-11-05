from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

url = "https://www.google.com/"
browser = webdriver.Chrome()
browser.get(url)

try:
    # Поиск поисковой строки
    search_box = browser.find_element(By.NAME, "q")  # Правильный селектор
    search_box.click()
    search_box.send_keys("Привет" + Keys.ENTER)

    # Ожидание появления первого результата поиска
    wait = WebDriverWait(browser, 10)  # Увеличено время ожидания
    first_result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3")))  # Используем h3 для заголовка результата

    # Извлечение текста первого результата
    extracted_text = first_result.text
    print(extracted_text)  # Вывод текста в консоль

finally:
    # Закрытие драйвера
    browser.quit()