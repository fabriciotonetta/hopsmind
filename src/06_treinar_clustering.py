import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
dados = pd.read_csv("dados/receitas_final.csv")

colunas_para_cluster = ["OG", "FG", "ABV", "IBU", "Color", "BoilSize", "BoilTime", "Efficiency"]
dados_numericos = dados[colunas_para_cluster]
scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(dados_numericos)

modelo_kmeans = KMeans(n_clusters=8, random_state=42, n_init=10)
dados["Cluster"] = modelo_kmeans.fit_predict(dados_padronizados)
    
print("Treinamento concluido!")
print("Quantidade de receitas por cluster:")
print(dados["Cluster"].value_counts().sort_index())

resumo_clusters = dados.groupby("Cluster")[colunas_para_cluster].mean().round(2)
print("Caracteristicas medias de cada cluster:")
print(resumo_clusters)
resumo_clusters.to_csv("dados/resumo_clusters.csv")
print("Resumo dos clusters salvo em dados/resumo_clusters.csv")