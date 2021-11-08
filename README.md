# Consulta de Processos Administrativos

## Prefeitura de Mauá

O *script* elaborado para automatização de [Consulta de Processos Administrativos](http://www.maua.sp.gov.br/eGoverno/Processo.aspx) da Prefeitura de Mauá no primeiro semestre de 2020. A pesquisa é feita inserindo o número do processo, o ano e cpf do interessado.

![sitemaua](https://i.imgur.com/VKTJkma.png)


------

## Como Usar?

Uma vez instalado o pacote, basta inserir os dados do processo que se deseja consultar.

```python
from maua import get_status

get_status(
    processo='456',
    ano=2021,
    cpf='417.892.372-20'
)
``` 