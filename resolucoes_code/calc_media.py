# Calculando a média de três notas fornecidas na entrada do usuário;

# Lista para armazenar os valores inseridos pelo usuário
valores = []

# Solicita ao usuário para inserir os valores
entrada = input("Digite os valores separados por vírgula por favor: ")
valores_str = entrada.split(',')

# Converte cada valor de string para inteiro e adiciona à lista
for valor_str in valores_str:
    valor = float(valor_str)
    valores.append(valor)

# Calcula a média dos valores
media = sum(valores) / len(valores)

# Imprime a média
print("A média dos valores é:", media)