# Conversor de Temperatura
temp = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (C/F/K): ").upper()
unidade_destino = input("Unidade de destino (C/F/K): ").upper()
resultado = None

if unidade_origem == unidade_destino:
    resultado = temp
elif unidade_origem == "C":
    if unidade_destino == "F":
        resultado = temp * 9/5 + 32
    elif unidade_destino == "K":
        resultado = temp + 273.15
elif unidade_origem == "F":
    if unidade_destino == "C":
        resultado = (temp - 32) * 5/9
    elif unidade_destino == "K":
        resultado = (temp - 32) * 5/9 + 273.15
elif unidade_origem == "K":
    if unidade_destino == "C":
        resultado = temp - 273.15
    elif unidade_destino == "F":
        resultado = (temp - 273.15) * 9/5 + 32

if resultado is not None:
    print(f"Temperatura convertida: {resultado:.2f} {unidade_destino}")
else:
    print("Conversão inválida.")
