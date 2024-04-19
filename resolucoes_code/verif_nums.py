# Verificando números pares e ímpares

num = input("Vamos verificar se o número é par ou ímpar? Digite: ")

# Tenta converter a entrada para um número de ponto flutuante
try:
    num = float(num)
    # Verifica se o número é um inteiro
    if num.is_integer():
        num = int(num)
        # Verifica se o número é par ou ímpar
        if num % 2 == 0:
            print(num, "é um número par.")
        else:
            print(num, "é um número ímpar.")
    else:
        print("Números decimais não funcionam, use um número inteiro.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número válido.")
