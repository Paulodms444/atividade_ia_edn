# Consulta de Cotação de Moeda na API AwesomeAPI
import requests
moeda = input("Digite o código da moeda (ex: USD, EUR): ").upper()
try:
    resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL")
    resposta.raise_for_status()
    dados = resposta.json()
    chave = f"{moeda}BRL"
    if chave in dados:
        info = dados[chave]
        print(f"Moeda: {info['code']} -> {info['codein']}")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Máxima: R$ {info['high']}")
        print(f"Mínima: R$ {info['low']}")
        print(f"Última atualização: {info['create_date']}")
    else:
        print("Moeda não encontrada.")
except Exception as e:
    print("Falha ao consultar a cotação.")
