# Média da Turma
notas = []
while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print("Entrada inválida. Tente novamente.")
if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota registrada.")
