# Calculadora de Dias de Vida
from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
try:
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.now()
    dias_vivo = (hoje - nascimento).days
    print(f"Você está vivo há {dias_vivo} dias.")
except ValueError:
    print("Data inválida. Use o formato dd/mm/aaaa.")
