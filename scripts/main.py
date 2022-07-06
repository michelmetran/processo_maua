#!/usr/bin/env python
# coding: utf-8


import os
from maua import Driver
from dotenv import dotenv_values, find_dotenv
from paths import driver_path

# Credentials
config = dotenv_values(find_dotenv())
os.environ['GH_TOKEN'] = config['GH_TOKEN']

# Driver
driver = Driver(headless=True, driver_path=None)

# Regularização
#CPF_MICHEL = config['CPF_MICHEL']
#driver.get_status('659', 2021, CPF_MICHEL)
#driver.get_status('660', 2021, CPF_MICHEL)
#driver.get_status('661', 2021, CPF_MICHEL)

# Processos Ambientais
CPF_ALBERTO = config['CPF_ALBERTO']
driver.get_status('6333', 2019, CPF_ALBERTO)  # Rancho Ypê
#driver.get_status('6334', 2019, CPF_ALBERTO)  # Rancho Sacy
