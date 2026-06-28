import pandas as pd

receitas_exoticas = [
    {"Name": "Cerveja de Jabuticaba", "Style": "Fruit Beer", "Size(L)": 20.0, "OG": 1.052, "FG": 1.012, "ABV": 5.2, "IBU": 12, "Color": 18, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Acai com Guarana", "Style": "Fruit Beer", "Size(L)": 20.0, "OG": 1.048, "FG": 1.011, "ABV": 4.8, "IBU": 10, "Color": 22, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Pequi", "Style": "Specialty Fruit Beer", "Size(L)": 20.0, "OG": 1.060, "FG": 1.014, "ABV": 6.0, "IBU": 25, "Color": 9, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Cupuacu", "Style": "Fruit Beer", "Size(L)": 20.0, "OG": 1.050, "FG": 1.012, "ABV": 5.0, "IBU": 14, "Color": 8, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Cafe com Pimenta Rosa", "Style": "Spice/Herb Beer", "Size(L)": 20.0, "OG": 1.065, "FG": 1.014, "ABV": 6.5, "IBU": 30, "Color": 35, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Maracuja com Mel", "Style": "Fruit Beer", "Size(L)": 20.0, "OG": 1.055, "FG": 1.012, "ABV": 5.5, "IBU": 15, "Color": 6, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Cacau e Canela", "Style": "Spice/Herb Beer", "Size(L)": 20.0, "OG": 1.070, "FG": 1.016, "ABV": 7.0, "IBU": 20, "Color": 32, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Abacaxi com Hortela", "Style": "Fruit Beer", "Size(L)": 20.0, "OG": 1.045, "FG": 1.010, "ABV": 4.5, "IBU": 8, "Color": 5, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Goiaba Vermelha", "Style": "Fruit Beer", "Size(L)": 20.0, "OG": 1.053, "FG": 1.012, "ABV": 5.3, "IBU": 11, "Color": 10, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Pimenta Biquinho", "Style": "Spice/Herb Beer", "Size(L)": 20.0, "OG": 1.062, "FG": 1.013, "ABV": 6.2, "IBU": 35, "Color": 7, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Mandioca Doce e Canela", "Style": "Specialty Beer", "Size(L)": 20.0, "OG": 1.058, "FG": 1.013, "ABV": 5.8, "IBU": 18, "Color": 14, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
    {"Name": "Cerveja de Castanha do Para", "Style": "Specialty Beer", "Size(L)": 20.0, "OG": 1.068, "FG": 1.015, "ABV": 6.8, "IBU": 22, "Color": 19, "BoilSize": 24.0, "BoilTime": 60, "Efficiency": 70.0, "BrewMethod": "All Grain", "SugarScale": "Specific Gravity"},
]

dados_exoticos = pd.DataFrame(receitas_exoticas)

print("Receitas exoticas criadas:", dados_exoticos.shape)
print(dados_exoticos.head())

dados_exoticos.to_csv("dados/receitas_exoticas.csv", index=False)
print("Arquivo salvo com sucesso em dados/receitas_exoticas.csv")

