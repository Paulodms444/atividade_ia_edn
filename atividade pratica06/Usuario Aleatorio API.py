# Consulta usuário fictício na API Random User Generator
import requests
try:
    resposta = requests.get("https://randomuser.me/api/")
    resposta.raise_for_status()
    dados = resposta.json()
    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")
except Exception as e:
    print("Falha ao acessar a API Random User Generator.")
