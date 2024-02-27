import pandas as pd 
import requests 
from plyer import notification
from datetime import datetime
import notificacao
import sqlite3
import re

#--------- FUNÇÕES GERAIS ----------------------------------------------------------

# Importando tabelas API
def importar (url):
    return requests.get(url)

# Formato data
def formato_datas():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Salvando a tabela em uma variável
def salvar_tabela(base):
    if base.status_code == 200:
        return base.json()

#------------- FUNÇÕES TABELA CORRETORAS -------------------------------------------

# Formatacao da coluna valor patrimonio
def formatar(valor):
    return "R${:,.2f}".format(valor)

def formato_valor(tabela,coluna):
    tabela[coluna] = pd.to_numeric(tabela[coluna])
    tabela[coluna] = tabela[coluna].apply(formatar)

# Formatacao das colunas com datas
def formato_data(tabela, coluna):
    tabela[coluna] = pd.to_datetime(tabela[coluna])
    tabela[coluna] = tabela[coluna].dt.strftime('%d-%m-%Y')

# Alterando o nome das colunas
def nome_colunas(tabela):
    return tabela.set_axis(['CNPJ', 'Tipo', 'Razão Social', 'Nome Comercial', 'Status', 'E-Mail', 'Telefone',
                          'CEP', 'Pais', 'UF', 'Municipio', 'Bairro', 'Complemento', 'Logradouro', 'Data Patrimonio', 
                          'Valor Patrimonio', 'Codigo CVM', 'Data Inicio', 'Data Registro'], axis=1)

# Exclusão de colunas irrelevantes para a análise. 
def exclusao_colunas(tabela):
     return tabela.drop(['Tipo','E-Mail', 'CEP', 'Complemento', 'Logradouro','Data Inicio',
                         'Data Patrimonio'], axis=1)

# Ajustando o Formato do CNPJ
def formato_cnpj(tabela,coluna):
    padrao = r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})'
    return tabela[coluna].str.replace(padrao, r'\1.\2.\3/\4-\5', regex = True)

# Filtro telefone
def filtro_str_len(tabela, coluna, length):
    return tabela[coluna].str.len() < length 

# Adicionando o 3 em telefones que estavam faltando 1 numero 
def ajuste_telefone(tabela, filtro, coluna):
    return '3'+ tabela.loc[filtro, coluna]

# Ajustando formato telefone
def formato_telefone(tabela, coluna):
    padrao_tel = r'(\d{4})(\d{4})'
    return tabela[coluna].str.replace(padrao_tel, r'\1-\2', regex=True)

# Funcao para filtrar string vazia
def string_vazia(tabela, coluna, length):
    return tabela[ tabela[coluna].str.len() == length].index

# Função drop de linhas 
def drop_linhas(tabela, filtro):
    return tabela.drop(filtro)

# Função filtrar caracteres especiais e valor zerado
def caracter_especial(tabela, coluna, condicional):
    return tabela[tabela[coluna] == condicional].index

# --------------- FUNÇÕES TABELA BANCOS --------------------------------------------

# Funcao para alterar nome das colunas

def altera_colunas(tabela):
    return tabela.set_axis(['ISPB', 'Nome', 'Código', 'Nome Completo'], axis=1)

#--------------- FUNÇÕES TABELA PIX ------------------------------------------------

# Funcao para alterar o nome das colunas
def modifica_coluna(tabela):
    return tabela.set_axis(['ISPB', 'Nome', 'Nome Reduzido', 'Modalidade', 'Tipo', 'Inicio'], axis=1)

# Funcao para ajustar o formato de data hora da coluna inicio
def ajusta_datahora(tabela, coluna):
    return tabela[coluna].dt.strftime('%d-%m-%Y %H:%M')
