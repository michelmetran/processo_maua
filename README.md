# Consulta de Processos Administrativos

<br>

Pense naquele processo administrativo, que é necessário acompanhar periodicamente!? Passei por isso com a [Consulta de Processos Administrativos](http://www.maua.sp.gov.br/eGoverno/Processo.aspx) da Prefeitura de Mauá e resolvi dinamizar a pesquisa processual.

No _site_ da Prefeitura é necessário inserir o número e ano do processo, bem como o CPF do interessado, conforme imagem abaixo.

![sitemaua](https://i.imgur.com/VKTJkma.png)

<br>

---

## Como Usar?

Uma vez instalado o pacote/módulo, basta inserir os dados do processo que se deseja consultar, conforme exemplo abaixo:

```python
from maua import get_status

get_status(
    processo='456',
    ano=2021,
    cpf='417.192.372-20'
)
```

<br>

É possível associar essa rotina a uma tecla de atalho e pronto: rapidamente torna-se possível consultar o _status_ do processo.
