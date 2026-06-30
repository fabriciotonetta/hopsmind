import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
chave_api = os.getenv("GOOGLE_API_KEY")

cliente = genai.Client(api_key=chave_api)

def gerar_rotulo(nome_cerveja, estilo):
    prompt = f"beer label design for '{nome_cerveja}', {estilo} style, artistic, vintage brewery label illustration, no text"
    print("Enviando pedido para a IA de imagem... aguarde")

    resposta = cliente.models.generate_content(
        model="gemini-3.1-flash-image",
        contents=[prompt],
    )

    for parte in resposta.candidates[0].content.parts:
        if parte.inline_data is not None:
            nome_arquivo = f"rotulos_gerados/{nome_cerveja.replace(' ', '_')}.png"
            with open(nome_arquivo, "wb") as f:
                f.write(parte.inline_data.data)
            print(f"Rotulo salvo para {nome_cerveja}")
            return

    print("Nenhuma imagem foi retornada. Resposta completa:", resposta)

gerar_rotulo("Cerveja de Jabuticaba", "Fruit Beer")