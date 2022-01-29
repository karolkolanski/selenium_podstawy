# Import biblioteki
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Otwarcie przeglądarki
driver = webdriver.Firefox()
# driver = webdriver.Chrome()

driver.get("https://www.kozminski.edu.pl/pl")

# Maksymalizacja okna
driver.maximize_window()

sleep(2)
# Odszukanie elementu
element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Studia podyplomowe')
element.click()

#driver.quit()
