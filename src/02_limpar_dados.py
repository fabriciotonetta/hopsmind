import pandas as pd

dados = pd.read_csv("dados/recipeData.csv", encoding="latin1")

colunas_uteis = ["Name", "Style", "Size(L)", "OG", "FG", "ABV", "IBU", "Color", "BoilSize", "BoilTime", "Efficiency", "BrewMethod", "SugarScale"]

dados = dados[colunas_uteis]

dados = dados.dropna(subset=["Name", "Style"])

print("Formato depois da limpeza:", dados.shape)
print("Valores vazios restantes:")
print(dados.isnull().sum())

dados.to_csv("dados/receitas_limpas.csv", index=False)

print("Arquivo salvo com sucesso em dados/receitas_limpas.csv")