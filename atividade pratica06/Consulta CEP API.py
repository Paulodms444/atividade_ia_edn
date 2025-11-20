# Consulta de CEP na API ViaCEP
import requests
cep = input("Digite o CEP (somente números): ")
try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    resposta.raise_for_status()
    dados = resposta.json()
    if 'erro' in dados:
        print("CEP não encontrado.")
    else:
        print(f"Logradouro: {dados.get('logradouro', '')}")
        print(f"Bairro: {dados.get('bairro', '')}")
        print(f"Cidade: {dados.get('localidade', '')}")
        print(f"Estado: {dados.get('uf', '')}")
except Exception as e:
    print("Falha ao consultar o CEP.")
