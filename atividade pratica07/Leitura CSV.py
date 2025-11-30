# Leitura de CSV e cálculo de média e soma
import csv
try:
    with open('dados.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        tempos = [float(row['tempo_execucao']) for row in reader]
    if tempos:
        media = sum(tempos) / len(tempos)
        total = sum(tempos)
        print(f"Média: {media:.2f}")
        print(f"Soma: {total:.2f}")
    else:
        print("Coluna tempo_execucao vazia.")
except Exception as e:
    print("Erro ao ler o arquivo CSV ou processar os dados.")
