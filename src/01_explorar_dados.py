import pandas as pd

caminho_arquivo = "dados/recipeData.csv"

dados = pd.read_csv(caminho_arquivo, encoding="latin1")

print("Quantidade de linhas e colunas:", dados.shape)

print("Nomes das colunas:", dados.columns.tolist())

print("Primeiras 5 receitas:")
print(dados.head())

print("Valores vazios por coluna:")
print(dados.isnull().sum())