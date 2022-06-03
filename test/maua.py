#!/usr/bin/env python
# coding: utf-8

import os
import time
from traquitanas import net
from bs4 import BeautifulSoup
from dotenv import dotenv_values, find_dotenv


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_status(processo, ano, cpf):
    # Driver
    driver = net.scraping.create_driver(
        download_path=os.getcwd(),
        headless=True,
        adds_path=os.path.join('..', 'scrapy', 'adds'),
        log_path=os.path.join('..', 'scrapy', 'logs'),
    )

    # Get URL
    # url = 'http://www.maua.sp.gov.br/eGoverno/Processo.aspx'
    # driver.get(url)
    # time.sleep(5)
    url = 'https://e-gov.maua.sp.gov.br/grp/acessoexterno/programaAcessoExterno.faces?codigo=70043'
    driver.get(url)
    time.sleep(5)

    # Insere Ano
    ex_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='form:exercicio:field']")))
    ex_field.send_keys(ano)
    #time.sleep(1)

    # Insere Numero
    n_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='form:numero:field']")))
    n_field.send_keys(processo)
    #time.sleep(1)

    # Insere CPF
    cpf_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='form:nome:field']")))
    cpf_field.send_keys(cpf)
    #time.sleep(0.1)

    # Clica para Pesquisar
    btn_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="form:j_id_3u:0:j_id_3y"]')))
    btn_field.click()
    time.sleep(3)

    # Get HTML
    soup = BeautifulSoup(driver.page_source, features='html.parser')

    # Get Results
    results = soup.find('span', attrs={'id': 'form:resultado'})
    results = results.get_text(separator='<b>').split('<b>')

    # Fix for Print
    for i in results:
        print(i.strip())

    # Close Driver
    driver.quit()
    
    # Print
    print('-'*50)

