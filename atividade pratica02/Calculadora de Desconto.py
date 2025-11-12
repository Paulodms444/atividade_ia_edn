# Calculadora de Desconto
produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

desconto = round(preco_original * desconto_percentual / 100, 2)
preco_final = round(preco_original - desconto, 2)

print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
