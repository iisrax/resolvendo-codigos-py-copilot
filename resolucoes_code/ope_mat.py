# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Primeiro número da equação: "))
num2 = int(input("Segundo número da equaçãoo: "))

operacao = input("Digite o tipo de operação desejada (+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)

elif operacao == '-':
    print(num1 - num2)

elif operacao == '*':
    print(num1 * num2)

elif operacao == '/':
    print(num1 / num2)

else:
    print("Uso incorreto de sinal. Tente usar '+' para soma, '-' para subtração, '*' para multiplicação e '/' para divisão.") 