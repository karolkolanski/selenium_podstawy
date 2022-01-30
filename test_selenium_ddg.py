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
element.send_keys("tester kozminski")
element.submit()

# "lamerskie" rozwiązanie
# sleep(4)

# Bardziej profesjonalne rozwiązanie
# Maksymalny czas oczekiwania na element
# (jeśli znajdzie szybcoiej, to poleci dalej)
driver.implicitly_wait(40)
# find_elements zwraca listę elementów
elements = driver.find_elements(By.XPATH, '//h2[@class="result__title js-result-title"]')
driver.implicitly_wait(0)

for el in elements:
    print(el.text)
# Śpię 3 sekundy, aby zobaczyć co się stało
sleep(3)

