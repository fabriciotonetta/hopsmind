import pandas as pd

dados_reais = pd.read_csv("dados/receitas_limpas.csv")
dados_exoticos = pd.read_csv("dados/receitas_exoticas.csv")

dados_final = pd.concat([dados_reais, dados_exoticos], ignore_index=True)

print("Dataset final:", dados_final.shape)
print("Ultimas 12 linhas (devem ser as receitas exoticas):")
print(dados_final.tail(12)[["Name", "Style", "ABV", "IBU"]])

dados_final.to_csv("dados/receitas_final.csv", index=False)
print("Dataset final salvo em dados/receitas_final.csv")
