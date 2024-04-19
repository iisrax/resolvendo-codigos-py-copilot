# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

# Solicita ao usuário que insira seu nome e armazena a entrada em uma variável
nome = input("Por favor, digite seu nome: ")
nome1 = input("Por favor, digite seu sobrenome: ") 

# Imprime uma mensagem de boas-vindas usando o nome fornecido pelo usuário
print("Olá,", nome + ' ' + nome1, "! Bem-vindo a Vila Oculta da Folha!")
