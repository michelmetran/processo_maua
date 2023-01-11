"""
Sistema de consulta aos Processos Administrativos da
Prefeitura de Mauá, SP, utilizando técnicas de webscrapping
"""

from dotenv import dotenv_values, find_dotenv
from maua.maua import Driver
from maua.paths import driver_path, logs_path

# Credentials
config = dotenv_values(find_dotenv())
CPF_ADMIN = config['CPF_ADMIN']
CPF_AMBIENTE = config['CPF_AMBIENTE']

# Driver
driver = Driver(
    my_driver_path=driver_path,
    my_logs_path=logs_path,
    verify_ssl=True,
)

# Regularização
# driver.get_status(processo='659', ano=2021, cpf=CPF_ADMIN)
# driver.get_status(processo='660', ano=2021, cpf=CPF_ADMIN)
# driver.get_status(processo='661', ano=2021, cpf=CPF_ADMIN)

# Compensação
driver.get_status(processo='6333', ano=2019, cpf=CPF_AMBIENTE)  # Ypê
# driver.get_status(processo='6334', ano=2019, cpf=CPF_AMBIENTE)  # Sacy

if __name__ == '__main__':
    print('Fim!')
