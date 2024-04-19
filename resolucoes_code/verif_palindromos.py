# Testando se uma palavra é um palíndromo;

def eh_palindromo(s):
    # Verifica se a string está vazia
    if not s.strip():
        return False
    
    # Remove espaços em branco e converte para minúsculas
    s = s.replace(" ", "").lower()
    
    # Verifica se a string contém apenas letras
    if not s.isalpha():
        return False
    
    # Inverte a string
    s_invertida = s[::-1]
    
    # Verifica se a string original é igual à string invertida
    return s == s_invertida

# Resultado
string = input("Digite uma palavra/frase: ")
if eh_palindromo(string):
    print("A palavra/frase é um palíndromo.")
else:
    print("Por favor, use palavras e frases sem acentos para verificação correta da mesma. ")

# Exemplo de palíndromo: A grama é amarga.