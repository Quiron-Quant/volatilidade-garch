import pandas as pd
import yfinance as yf
import numpy as np
import os


#Configuracões inicais(testes)
TICKERS = ["^BVSP", "PETR4.SA", "VALE3.SA"]
INICIO = "2010-01-01"
FIM = "2026-10-31"

def baixar_precos(tickers, inicio, fim):
    """Baixa os preços de fechamento ajustados de cada ativo."""
    dados = yf.download(tickers, start = inicio, end = fim, auto_adjust = True, progress = False) #Retorna uma DataFrame
    precos =  dados["Close"] #Recorta o DataFrame para apenas os precos de fechamento
    return precos

def limpar_precos(precos):
    """Retira os dias que os precos não existem na Ibovespa. Normalmente feriados com preços espelhados"""
    precos = precos.dropna(subset=["^BVSP"])
    return precos

def calcular_retornos(precos):
    """Calcula o log retorno (r_t = ln(P_t) - ln(P_t-1))"""
    precos_dia_anterior = precos.shift(1) #Joga os precos em uma linha para baixo, o preco de ontem vira o de hoje
    log_precos = np.log(precos) #Calcula o logaritmo natural de todos os precos
    log_precos_dia_anterior = np.log(precos_dia_anterior) #Calcula o logaritmo natural de todos os precos do dia anterior
    retorno = log_precos - log_precos_dia_anterior #Calcula o retorno a partir de uma propriedade de logaritmos

    retorno = retorno.iloc[1:] #Todas as linhas menos a primeira (não há retorno do primeiro dia, pois não há dia anterior)

    return retorno

def salvar_dados(precos, retorno):
    """Salva os dados de preços e retornos em um arquivo do tipo Parquet"""
    os.makedirs("data", exist_ok=True) #Cria um novo diretório

    retorno.to_parquet("data/retornos.parquet") #Salva os retorono em um arquivo parquet
    precos.to_parquet("data/precos.parquet") #Salva os precos em um arquivo parquet
    #Parquet -> um tipo de arquivo binario parecido com CSV que guarda etiquetas para cada tipo de elemento, podendo ser transfomrado em um DataFrame



if __name__ == "__main__":
    precos = baixar_precos(TICKERS, INICIO, FIM)
    precos = limpar_precos(precos)

    print(precos.head()) #Acessa as primeiras n linhas da tabela. Sem argumento, são as 5 primeiras
    print(precos.tail()) #Acessa as ultimas n linhas da tabela. Sem argumento, são as 5 últimas
    print(precos.shape) #Devolve uma tupla de dois elementos, sendo a quantidade de linahas e colunas, respectivamente
    print(precos.isna().sum()) #Conta e soma a quantidade de elementos NaN (Not a Number)
    print(precos[precos["^BVSP"].isna()]) #Usa os dias em que a função "isna" devolve True como filtro

    retorno = calcular_retornos(precos)

    salvar_dados(precos, retorno)

    print(retorno.head())


    

