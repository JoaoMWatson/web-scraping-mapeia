import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

elements = [{}]

# 1. Abrir navegador com o site
url = "https://www.mapeia.com.br/"

options = Options()
options.headless = True
driver = webdriver.Firefox()

driver.get(url)
time.sleep(5)

# 2. Localizar os inputs
elements.append("origin":driver.find_element_by_id("origin"))
elements.append("destination":driver.find_element_by_id("destination"))
elements.append("fuel-price":driver.find_element_by_id("fuel-price"))
elements.append("fuel-comsuption":driver.find_element_by_id("fuel-comsuption"))

print(elements)


# 3. Preencher os inputs

# 4. Pegar resultados

# 5. Tratar dados
# 6. Gerar json


driver.quit()
