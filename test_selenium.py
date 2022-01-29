# Import biblioteki
from selenium import webdriver

# Otwarcie przeglądarki
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
#Otwarcie strony wp.pl
driver.get("http://www.wp.pl")