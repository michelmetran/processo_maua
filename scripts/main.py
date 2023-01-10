"""
dddd
"""

from dotenv import dotenv_values, find_dotenv
from maua import Driver
from paths import driver_path, logs_path

# Credentials
config = dotenv_values(find_dotenv())
CPF_MICHEL = config['CPF_MICHEL']
CPF_ALBERTO = config['CPF_ALBERTO']

# Driver
driver = Driver(
    my_driver_path=driver_path,
    my_logs_path=logs_path,
    verify_ssl=True,
)

# Regularização
# driver.get_status('659', 2021, CPF_MICHEL)
# driver.get_status('660', 2021, CPF_MICHEL)
# driver.get_status('661', 2021, CPF_MICHEL)

# Processos Ambientais
driver.get_status('6333', 2019, CPF_ALBERTO)  # Rancho Ypê
#driver.get_status('6334', 2019, CPF_ALBERTO)  # Rancho Sacy

if __name__ == '__main__':
    print('Fim!')
