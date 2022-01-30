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

# Śpię 3 sekundy, aby zobaczyć co się stało
sleep(3)