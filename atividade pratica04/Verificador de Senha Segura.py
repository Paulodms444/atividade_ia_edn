# Verificador de Senha Segura
senha = input("Digite a senha: ")
criterio_tamanho = len(senha) >= 8
criterio_numero = any(char.isdigit() for char in senha)

if criterio_tamanho and criterio_numero:
    print("Senha válida!")
else:
    print("Senha inválida. Deve ter pelo menos 8 caracteres e conter pelo menos um número.")
