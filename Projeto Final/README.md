## **Projeto Final Python**

Projeto final do curso de Python da CoderHouse. Esse projeto tem por objetivo desenvolver um pipeline de dados, onde foram realizados
a extração dos dados brutos via API, tratamento dos dados visando obter dados mais consistentes para serem analisados, a criação de um
banco de dados e o armazenamento das tabelas nesse banco. 

## :pencil: **Pré-requisitos**

:arrow_right: [Python 3](https://www.python.org/downloads/)

:arrow_right: [Visual Studio Code](https://code.visualstudio.com/download)

:heavy_exclamation_mark:É necessário baixar o arquivo [notificacao.py](https://github.com/iago-cord/Curso-Python/blob/main/Projeto%20Final/requirements.txt) e [funcoes.py](https://github.com/iago-cord/Curso-Python/blob/main/Projeto%20Final/funcoes.py) para que o código funcione corretamente. 

## :notebook_with_decorative_cover: Bibliotecas Utilizadas

As bibliotecas utilizadas no projeto estão disponiveis no arquivo [requirements.txt](https://github.com/iago-cord/Curso-Python/blob/main/Projeto%20Final/requirements.txt)
Nesse arquivo você pode conferir as bibliotecas e versões utilizadas. 

## :fuelpump: API's 

Para o desenvolvimento do projeto, foram utilizadas 3 bases de dados, disponibilizados pela **Brasil API**, que tem como como objetivo 
compilar dados sobre diversas áreas do pais. 
**Foram utilizadas 3 API's:**

:arrow_right: [**Corretoras**](https://brasilapi.com.br/api/cvm/corretoras/v1)

Fornece uma lista de todas as corretoras cadastradas na CVM, estando elas ativas ou canceladas. 

:arrow_right: [**Bancos**](https://brasilapi.com.br/api/banks/v1)

Fornece uma lista de todos os bancos operantes no Brasil.

:arrow_right: [**PIX**](https://brasilapi.com.br/api/pix/v1/participants)

Fornece uma lista de todos os bancos participantes do PIX no Brasil.

## :clipboard: Documentação

Este projeto está dividido em três arquivos, [Projeto Final.ipynb](https://github.com/iago-cord/Curso-Python/blob/main/Projeto%20Final/Projeto%20Final.ipynb) onde foi realizado a extração e a transformação dos dados, [notificação.py](https://github.com/iago-cord/Curso-Python/blob/main/Projeto%20Final/notificacao.py) que notifica se a importação da API obteve sucesso ou não e [funcoes.py](https://github.com/iago-cord/Curso-Python/blob/main/Projeto%20Final/funcoes.py) onde estão as funções utilizadas para a extração e transformação dos dados. 

:arrow_right: Importando tabelas das API's -> função para importar as url's das API's recebe como parametro a url e retorna o request. 

##### Função
def importar (url):
    return requests.get(url)

##### *Extraindo a tabela banks da API
*url = "https://brasilapi.com.br/api/banks/v1"*

*bancos = func.importar(url)*

##### *Extraindo a tabela corretoras da API*
*url = "https://brasilapi.com.br/api/cvm/corretoras/v1"*

*corretoras = func.importar(url)*

##### *Extraindo a tabela PIX da API*
*url = 'https://brasilapi.com.br/api/pix/v1/participants'*

*pix = requests.get(url)*
