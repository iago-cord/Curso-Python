import pandas as pd 
import requests 
from plyer import notification
from datetime import datetime
import notificacao
import sqlite3
import re

#--------- FUNÇÕES GERAIS ----------------------------------------------------------

# Importando tabelas API -> função para importar as url's das API's recebe como parametro a url e retorna o 
# request. 
def importar (url):
    return requests.get(url)

# Formato data -> Foi usado o metodo strftime para transformar o objeto em string e formatar a data
# e hora no formato correto
def formato_datas():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Salvando a tabela em uma variável -> Essa função recebe como parametro a base de dados, verifica se o status
# code é igual a 200 e retorna a base passada como parametro no formato .json
def salvar_tabela(base):
    if base.status_code == 200:
        return base.json()

#------------- FUNÇÕES TABELA CORRETORAS -------------------------------------------

# Formatacao da coluna valor patrimonio -> Foi utilizado o Regex para determinar a fomatacao, o metodo
# format() que vai receber a coluna a ser modificada. Depois criamos a função formato_valor que vai receber como 
# parametro o dataframe e a coluna, foi utilizado o pd.to_numeric para transformar o objeto em um numerico e depois 
# o metodo .apply que recebeu a função formatar para aplicar a formatação a cada elemento da coluna.
def formatar(valor):
    return "R${:,.2f}".format(valor)

def formato_valor(tabela,coluna):
    tabela[coluna] = pd.to_numeric(tabela[coluna])
    tabela[coluna] = tabela[coluna].apply(formatar)

# Formatacao das colunas com datas -> Recebe como parametro o dataframe e a coluna a ser modificada, utiliza o 
# metodo pd.to_datetime para transformar o dataframe em um objeto do tipo datetime, depois foi aplicado o metodo
# dt.strftime para formatar esse objeto. 
def formato_data(tabela, coluna):
    tabela[coluna] = pd.to_datetime(tabela[coluna])
    tabela[coluna] = tabela[coluna].dt.strftime('%d-%m-%Y')

# Alterando o nome das colunas -> Passamos como parametro o dataframe, foi usado o metodo set_axis que recebeu 
# como parametro as colunas a serem alteradas e o eixo(axis) 0 para linhas e 1 para colunas, no caso como 
# foi alterado o nome da coluna passamos o axis=1
def nome_colunas(tabela):
    return tabela.set_axis(['CNPJ', 'Tipo', 'Razão Social', 'Nome Comercial', 'Status', 'E-Mail', 'Telefone',
                          'CEP', 'Pais', 'UF', 'Municipio', 'Bairro', 'Complemento', 'Logradouro', 'Data Patrimonio', 
                          'Valor Patrimonio', 'Codigo CVM', 'Data Inicio', 'Data Registro'], axis=1)

# Exclusão de colunas irrelevantes para a análise. -> Recebe o dataframe como parametro, com o metodo .drop
# especificamos os nomes das colunas a serem dropadas, e o eixo de exclusão axis=1
def exclusao_colunas(tabela):
     return tabela.drop(['Tipo','E-Mail', 'CEP', 'Complemento', 'Logradouro','Data Inicio',
                         'Data Patrimonio'], axis=1)

# Ajustando o Formato do CNPJ -> recebe o dataframe e a coluna como parametro, depois determinamos o padrão atraves
# do regex, o str.replace recebe o padrao para identificar e modificar os padroes na coluna, em seguida o padrão
# de modificao para o CNPJ e o regex=true para informar que se trata de uma expressão regular.
def formato_cnpj(tabela,coluna):
    padrao = r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})'
    return tabela[coluna].str.replace(padrao, r'\1.\2.\3/\4-\5', regex = True)

# Filtro telefone - Passamos como parametro o dataframe, a coluna e nesse caso o tamanho(length) da string a ser filtrada
# o metodo str.len transforma o objeto em string e faz a contagem do tamanho, e retorna os elementos da coluna 
# que atendem o tamanho passado no parametro length. 
def filtro_str_len(tabela, coluna, length):
    return tabela[coluna].str.len() < length 

# Adicionando o 3 em telefones que estavam faltando 1 numero  - Recebe de parametro o dataframe, o filtro e a coluna
# o metodo .loc vai selecionar as linhss que atendem ao filtro e adicionar o numero 3 na frente desses numeros. 
def ajuste_telefone(tabela, filtro, coluna):
    return '3'+ tabela.loc[filtro, coluna]

# Ajustando formato telefone -> dataframe e coluna como parametro, depois definimos o padrao atraves do regex para identificar
# depois o str.replace recebe o padrao definido, a formatacao a ser aplicada e regex=true para informar que se
# trata de uma expressão regular
def formato_telefone(tabela, coluna):
    padrao_tel = r'(\d{4})(\d{4})'
    return tabela[coluna].str.replace(padrao_tel, r'\1-\2', regex=True)

# Funcao para filtrar string vazia - recebe como parametro dataframe, coluna e o tamanho da string. o metodo
# str.len transforma o objeto em string faz a contagem e retorna o index da linha que atende a condição especificada. 
def string_vazia(tabela, coluna, length):
    return tabela[ tabela[coluna].str.len() == length].index

# Função drop de linhas - recebe como parametro o dataframe e o filtro anterior que retorna o index, o metodo drop
# recebe o filtro como condição e dropa todas as linhas que atendem a condição do filtro baseado no index. 
def drop_linhas(tabela, filtro):
    return tabela.drop(filtro)

# Função filtrar caracteres especiais e valor zerado - recebe como parametro o dataframe, a coluna e o caracter 
# a ser condicionado, depois retorna o index de todas as linhas que atendem a condicional.
def caracter_especial(tabela, coluna, condicional):
    return tabela[tabela[coluna] == condicional].index

# --------------- FUNÇÕES TABELA BANCOS --------------------------------------------

# Funcao para alterar nome das colunas -> Passamos como parametro o dataframe, foi usado o metodo set_axis que recebeu 
# como parametro as colunas a serem alteradas e o eixo(axis) 0 para linhas e 1 para colunas, no caso como 
# foi alterado o nome da coluna passamos o axis=1
def altera_colunas(tabela):
    return tabela.set_axis(['ISPB', 'Nome', 'Código', 'Nome Completo'], axis=1)

#--------------- FUNÇÕES TABELA PIX ------------------------------------------------

# Funcao para alterar o nome das colunas -> Passamos como parametro o dataframe, foi usado o metodo set_axis que recebeu 
# como parametro as colunas a serem alteradas e o eixo(axis) 0 para linhas e 1 para colunas, no caso como 
# foi alterado o nome da coluna passamos o axis=1
def modifica_coluna(tabela):
    return tabela.set_axis(['ISPB', 'Nome', 'Nome Reduzido', 'Modalidade', 'Tipo', 'Inicio'], axis=1)

# Funcao para ajustar o formato de data hora da coluna inicio -> Recebe como parametro o dataframe e a coluna a ser modificada, utiliza o 
# metodo pd.to_datetime para transformar o dataframe em um objeto do tipo datetime, depois foi aplicado o metodo
# dt.strftime para formatar esse objeto. 
def ajusta_datahora(tabela, coluna):
    return tabela[coluna].dt.strftime('%d-%m-%Y %H:%M')
