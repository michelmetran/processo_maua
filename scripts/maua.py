"""
dddd
"""

import time
from bs4 import BeautifulSoup
from dotenv import dotenv_values, find_dotenv


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager


from paths import *


class Driver():
    # Conceito de Page Object Model (POM)
    def __init__(self, headless, driver_path):
        # Cria Driver
        firefox_options = FirefoxOptions()
        firefox_options.headless = headless
        driver = webdriver.Firefox(
            service=Service(
                executable_path=GeckoDriverManager(path=driver_path).install(),
                log_path=log_path / 'geckodriver.log',
            ),
            options=firefox_options,
        )
        self.driver = driver

    def get_status(self, processo, ano, cpf):
        # Get URL
        url = 'https://e-gov.maua.sp.gov.br/grp/acessoexterno/programaAcessoExterno.faces?codigo=70043'
        self.driver.get(url)

        # Insere Ano
        ex_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='form:exercicio:field']")))
        ex_field.send_keys(ano)

        # Insere Numero
        n_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='form:numero:field']")))
        n_field.send_keys(processo)

        # Insere CPF
        cpf_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='form:nome:field']")))
        cpf_field.send_keys(cpf)

        # Clica para Pesquisar
        btn_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="form:j_id_3u:0:j_id_3y"]')))
        btn_field.click()
        time.sleep(3)

        # Get HTML
        soup = BeautifulSoup(self.driver.page_source, features='html.parser')

        # Get Results
        results = soup.find('span', attrs={'id': 'form:resultado'})
        results = results.get_text(separator='<b>').split('<b>')

        # Fix for Print
        for i in results:
            print(i.strip())

        # Close Driver
        self.driver.quit()

