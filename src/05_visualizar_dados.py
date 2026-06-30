import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("dados/receitas_final.csv")

top_estilos = dados["Style"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_estilos.values, y=top_estilos.index, hue=top_estilos.index, palette="viridis", legend=False)
plt.title("Os 10 Estilos de Cerveja Mais Comuns no Dataset")
plt.xlabel("Quantidade de Receitas")
plt.ylabel("Estilo")
plt.tight_layout()

plt.savefig("prints/grafico_top_estilos.png")
print("Grafico salvo em prints/grafico_top_estilos.png")

plt.figure(figsize=(10, 6))
sns.histplot(dados["ABV"], bins=50, kde=True, color="darkorange")
plt.title("Distribuicao do Teor Alcoolico (ABV) das Receitas")
plt.xlabel("ABV (%)")
plt.ylabel("Quantidade de Receitas")
plt.xlim(0, 20)
plt.tight_layout()
plt.savefig("prints/grafico_distribuicao_abv.png")
print("Grafico salvo em prints/grafico_distribuicao_abv.png")

plt.figure(figsize=(10, 6))
amostra = dados.sample(n=3000, random_state=42)
sns.scatterplot(data=amostra, x="Color", y="IBU", alpha=0.4, color="steelblue")
plt.title("Relacao entre Cor e Amargor (IBU) das Cervejas")
plt.xlabel("Cor (escala SRM)")
plt.ylabel("Amargor (IBU)")
plt.xlim(0, 40)
plt.ylim(0, 120)
plt.tight_layout()
plt.savefig("prints/grafico_cor_vs_ibu.png")
print("Grafico salvo em prints/grafico_cor_vs_ibu.png")