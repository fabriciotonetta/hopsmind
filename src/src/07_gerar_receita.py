import pandas as pd
import numpy as np

dados = pd.read_csv("dados/receitas_final.csv")
resumo_clusters = pd.read_csv("dados/resumo_clusters.csv", index_col="Cluster")

def gerar_receita_nova(cluster_escolhido, nome_receita):
    perfil = resumo_clusters.loc[cluster_escolhido]
    
    nova_receita = {
        "Name": nome_receita,
        "OG": round(np.random.normal(perfil["OG"], 0.005), 3),
        "FG": round(np.random.normal(perfil["FG"], 0.003), 3),
        "ABV": round(np.random.normal(perfil["ABV"], 0.5), 1),
        "IBU": round(np.random.normal(perfil["IBU"], 5), 1),
        "Color": round(np.random.normal(perfil["Color"], 2), 1),
        "BoilSize": round(np.random.normal(perfil["BoilSize"], 2), 1),
        "BoilTime": int(perfil["BoilTime"]),
        "Efficiency": round(perfil["Efficiency"], 1),
    }
    return nova_receita
receita_teste = gerar_receita_nova(cluster_escolhido=1, nome_receita="Cerveja Gerada por IA - Teste 1")
print(receita_teste)