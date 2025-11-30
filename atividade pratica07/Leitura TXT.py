# Leitura de arquivo TXT linha a linha
try:
    nome_arquivo = input("Digite o nome do arquivo para ler: ")
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            print(linha.strip())
except Exception as e:
    print("Erro ao ler o arquivo.")
