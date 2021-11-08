#!/usr/bin/env python
# coding: utf-8

import os
import time
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver():
    # Driver Firefox com Profile
    profile = webdriver.FirefoxProfile()
    profile.set_preference('intl.accept_languages', 'pt-BR, pt')
    profile.update_preferences()

    # Driver Firefox com Options
    options = Options()
    options.headless = True

    # Driver
    log_path = os.path.join('..', 'logs')
    os.makedirs(log_path, exist_ok=True)
    driver = webdriver.Firefox(
        firefox_profile=profile,
        options=options,
        service_log_path=os.path.join(log_path, 'geckodriver.log')
    )
    return driver


def get_status(processo, ano, cpf):
    # Get URL
    driver = create_driver()
    url = 'http://www.maua.sp.gov.br/eGoverno/Processo.aspx'
    driver.get(url)
    time.sleep(5)
    url = 'https://e-gov.maua.sp.gov.br/grp/acessoexterno/programaAcessoExterno.faces?codigo=70043'
    driver.get(url)
    time.sleep(5)

    # Insere Ano
    ex_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='form:exercicio:field']")))
    ex_field.send_keys(ano)
    time.sleep(1)

    # Insere Numero
    n_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='form:numero:field']")))
    n_field.send_keys(processo)
    time.sleep(1)

    # Insere CPF
    cpf_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='form:nome:field']")))
    cpf_field.send_keys(cpf)
    time.sleep(1)

    # Clica para Pesquisar
    btn_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='form:j_id_3p:0:j_id_3t']")))
    btn_field.click()
    time.sleep(5)

    # Get HTML
    soup = BeautifulSoup(driver.page_source, features='html.parser')

    # Get Results
    results = soup.find('span', attrs={'id': 'form:resultado'})
    results = results.get_text(separator='<b>').split('<b>')

    # Fix for Print
    for i in results:
        print(i.strip())

    # Close Driver
    driver.close()
    
    # Print
    print('-'*50)




