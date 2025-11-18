# Classificador de Pares e Ímpares
pares = 0
impares = 0
while True:
    entrada = input("Digite um número (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        print("Entrada inválida. Tente novamente.")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
