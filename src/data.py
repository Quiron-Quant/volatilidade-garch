import pandas as pd
import yfinance as yf


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


if __name__ == "__main__":
    precos = baixar_precos(TICKERS, INICIO, FIM)
    precos = limpar_precos(precos)
    print(precos.head()) #Acessa as primeiras n linhas da tabela. Sem argumento, são as 5 primeiras
    print(precos.tail()) #Acessa as ultimas n linhas da tabela. Sem argumento, são as 5 últimas
    print(precos.shape) #Devolve uma tupla de dois elementos, sendo a quantidade de linahas e colunas, respectivamente
    print(precos.isna().sum()) #Conta e soma a quantidade de elementos NaN (Not a Number)
    print(precos[precos["^BVSP"].isna()]) #Usa os dias em que a função "isna" devolve True como filtro
    

