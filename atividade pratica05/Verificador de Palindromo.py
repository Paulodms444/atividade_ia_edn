# Função para verificar palíndromo
def eh_palindromo(texto: str) -> bool:
    texto_filtrado = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_filtrado == texto_filtrado[::-1]

entrada = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(entrada)
print("Sim" if resultado else "Não")
