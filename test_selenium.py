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
element = driver.find_element_by_id('search_form_input_homepage')
print(type(element))
print(element.tag_name)

driver.quit()
