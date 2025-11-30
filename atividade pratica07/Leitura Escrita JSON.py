# Leitura e escrita de arquivo JSON
import json
pessoa = {"nome": "Lucas", "idade": 28, "cidade": "Curitiba"}
nome_arquivo = "pessoa.json"
try:
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(pessoa, f, ensure_ascii=False, indent=4)
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    print("Dados lidos do JSON:")
    print(dados)
except Exception as e:
    print("Falha ao salvar ou ler o arquivo JSON.")
