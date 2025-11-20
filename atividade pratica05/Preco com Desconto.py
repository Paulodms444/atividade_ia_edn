# Calculadora de Preço com Desconto
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite a porcentagem de desconto: "))
valor_desconto = preco * (desconto / 100)
preco_final = round(preco - valor_desconto, 2)
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
