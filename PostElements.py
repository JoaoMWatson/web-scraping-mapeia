import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


class PostElements():
    def __init__(self,
                 saida,
                 destino,
                 valorCombustivel,
                 consumoDeCombustivel):

        self.saida = saida
        self.destino = destino
        self.valorCombustivel = valorCombustivel
        self.consumoDeCombustivel = consumoDeCombustivel
        self.url = "https://www.mapeia.com.br/"

        self.__elements = []

        options = Options()

        options.headless = True
        self.__driver = webdriver.Firefox()

        self.__driver.get(self.url)
        time.sleep(3)

        self._setElements()


    def _setElements(self):
        try:
            self.__elements.append(
                self.__driver.find_element_by_id("origin"))
            self.__elements.append(
                 self.__driver.find_element_by_id("destination"))
            self.__elements.append(
                 self.__driver.find_element_by_id("fuel-price"))
            self.__elements.append(
                 self.__driver.find_element_by_id("fuel-consumption"))

            self.__writeIntoElements(self.saida,
                                     self.destino,
                                     self.valorCombustivel,
                                     self.consumoDeCombustivel)

        except Exception as e:
            raise Exception
            print(f"[{e.args}]")

        # finally:
            # self.__driver.quit()

    def __writeIntoElements(self, *elementValues):

        for _ in range(0, 4):
            self.__elements[_].send_keys(elementValues[_])
            time.sleep(3)
            self.__elements[_].send_keys(Keys.ENTER)
        
        calcButtom = self.__driver.find_element_by_id("calc")
        calcButtom.send_keys(Keys.ENTER)


PostElements("São Paulo", "Ceará", "1.00", "10.00")
