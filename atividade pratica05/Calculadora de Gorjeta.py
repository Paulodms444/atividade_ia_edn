# Função para calcular gorjeta
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100)

# Exemplo de uso
valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
