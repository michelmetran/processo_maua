"""
dddd
"""

import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from traquitanas.scrapping import gecko

#from dotenv import dotenv_values, find_dotenv
#from paths import driver_path, logs_path



class Driver(webdriver.Firefox):
    """
    Cria driver customizado do Selenium

    :param webdriver: _description_
    :type webdriver: _type_
    """

    def __init__(self, my_driver_path, my_logs_path, *args, **kwargs):
        """

        verify_ssl

        :param my_driver_path: _description_
        :type my_driver_path: pathlib
        :param my_logs_path: _description_
        :type my_logs_path: pathlib
        """
        # Services
        gecko_path = gecko.get_path_geckodriver(
            my_driver_path, verify_ssl=kwargs['verify_ssl']
        )

        # Logs
        logs_filepath = my_logs_path / 'geckodriver.log'

        # Services
        my_service = FirefoxService(
            executable_path=gecko_path, log_path=logs_filepath
        )

        # Options
        my_options = FirefoxOptions()
        my_options.headless = True
        my_options.set_preference('intl.accept_languages', 'pt-BR, pt')

        # Driver
        my_driver = super(Driver, self)
        my_driver.__init__(service=my_service, options=my_options)

    def add_extension_xpath(self, my_adds_path):
        """
        Adiciona Xpath extension

        :param my_adds_path: Pasta da Extensão
        :type my_adds_path: pathlib
        """
        adds.add_extension_xpath(self, my_adds_path)

    def get_status(self, processo, ano, cpf):
        """
        _summary_

        :param processo: _description_
        :type processo: _type_
        :param ano: _description_
        :type ano: _type_
        :param cpf: _description_
        :type cpf: _type_
        """
        # Get URL
        url = 'https://e-gov.maua.sp.gov.br/grp/acessoexterno/programaAcessoExterno.faces?codigo=70043'
        self.get(url)

        # Insere Ano
        ex_field = WebDriverWait(self, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='form:exercicio:field']")
            )
        )
        ex_field.send_keys(ano)

        # Insere Numero
        n_field = WebDriverWait(self, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='form:numero:field']")
            )
        )
        n_field.send_keys(processo)

        # Insere CPF
        cpf_field = WebDriverWait(self, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='form:nome:field']")
            )
        )
        cpf_field.send_keys(cpf)

        # Clica para Pesquisar
        btn_field = WebDriverWait(self, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="form:j_id_3u:0:j_id_3y"]')
            )
        )
        btn_field.click()
        time.sleep(3)

        # Get HTML
        soup = BeautifulSoup(self.page_source, features='html.parser')

        # Get Results
        results = soup.find('span', attrs={'id': 'form:resultado'})
        results = results.get_text(separator='<b>').split('<b>')

        # Fix for Print
        for i in results:
            print(i.strip())

        # Close Driver
        self.quit()


if __name__ == '__main__':
    print('Fim!!!!')
