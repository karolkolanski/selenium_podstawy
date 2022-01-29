# Import biblioteki
from selenium import webdriver
from selenium.webdriver.common.by import By

# Otwarcie przeglądarki
driver = webdriver.Firefox()
# driver = webdriver.Chrome()

#Otwarcie strony duckduckgo.com
driver.get("http://duckduckgo.com")

# Maksymalizacja okna
driver.maximize_window()

# Odszukanie elementu - pole wyszukiwania
# element = driver.find_element_by_id('search_form_input_homepage')  - selenium do 2021 roku
element = driver.find_element(By.ID, 'search_form_input_homepage')  #- selenium 4

# Wpisz teskt 'tester ALK' w pole wyszukiwania
element.send_keys("tester ALK")

#driver.quit()
