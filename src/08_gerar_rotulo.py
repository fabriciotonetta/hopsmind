import os
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": f"Bearer {token}"}

def gerar_rotulo(nome_cerveja, estilo):
    prompt = f"beer label design for '{nome_cerveja}', {estilo} style, artistic, vintage brewery label, illustration"
    print("Enviando pedido para a IA de imagem... aguarde")
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    print("Resposta recebida! Codigo:", response.status_code)
    if response.status_code == 200:
        with open(f"rotulos_gerados/{nome_cerveja.replace(' ', '_')}.png", "wb") as f:
            f.write(response.content)
        print(f"Rotulo salvo para {nome_cerveja}")
    else:
        print("Erro:", response.status_code, response.text)

gerar_rotulo("Cerveja de Jabuticaba", "Fruit Beer")