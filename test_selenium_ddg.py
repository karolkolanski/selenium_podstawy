# Import biblioteki
from selenium import webdriver
from selenium.webdriver.common.by import By
# dla explicit_wait
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Otwarcie przeglądarki
driver = webdriver.Firefox()

driver.get("https://duckduckgo.com/")

# Maksymalizacja okna
driver.maximize_window()

# Odszukanie elementu
element = driver.find_element(By.ID, 'search_form_input_homepage')
element.send_keys("tester kozminski")
element.submit()

# "lamerskie" rozwiązanie
# sleep(4)

# Bardziej profesjonalne rozwiązanie
# Maksymalny czas oczekiwania na element
# (jeśli znajdzie szybcoiej, to poleci dalej)
# driver.implicitly_wait(40)
# # find_elements zwraca listę elementów
# elements = driver.find_elements(By.XPATH, '//h2[@class="result__title js-result-title"]')
# driver.implicitly_wait(0)

# Explicit wait - czekanie na wystąpienie określonego warunku
wait = WebDriverWait(driver, 10)
elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//h2[@class="result__title js-result-title"]')))
# elements = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located((By.XPATH, '//h2[@class="result__title js-result-title"]')))

for el in elements:
    print(el.text)

# Śpię 3 sekundy, aby zobaczyć co się stało
sleep(3)
driver.quit()