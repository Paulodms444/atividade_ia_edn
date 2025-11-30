# Escrita de arquivo TXT tabular
try:
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.txt): ")
    pessoas = [
        {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
        {"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
        {"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"}
    ]
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(f"{'Nome':<10}{'Idade':<8}{'Cidade':<20}\n")
        for p in pessoas:
            f.write(f"{p['nome']:<10}{p['idade']:<8}{p['cidade']:<20}\n")
    print("Arquivo salvo com sucesso!")
except Exception as e:
    print("Falha ao salvar o arquivo.")
