# Import biblioteki
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Otwarcie przeglądarki
driver = webdriver.Firefox()

driver.get("https://duckduckgo.com/")

# Maksymalizacja okna
driver.maximize_window()

# Odszukanie elementu
element = driver.find_element(By.ID, 'search_form_input_homepage')
element.send_keys("tester ALK")
element.submit()

# "lamerskie" rozwiązanie
sleep(3)
# find_elements zwraca listę elementów
elements = driver.find_elements(By.XPATH, '//h2[@class="result__title js-result-title"]')

for el in elements:
    print(el.text)
# Śpię 3 sekundy, aby zobaczyć co się stało
sleep(3)

