import maua
from dotenv import dotenv_values, find_dotenv


# Credentials
config = dotenv_values(find_dotenv())
CPF_ALBERTO = config['CPF_ALBERTO']
CPF_MICHEL = config['CPF_MICHEL']


# Regularização
#maua.get_status('659', 2021, CPF_MICHEL)
#maua.get_status('660', 2021, CPF_MICHEL)
#maua.get_status('661', 2021, CPF_MICHEL)


# Processos Ambientais
maua.get_status('6333', 2019, CPF_ALBERTO)  # Rancho Ypê
#maua.get_status('6334', 2019, CPF_ALBERTO)  # Rancho Sacy
