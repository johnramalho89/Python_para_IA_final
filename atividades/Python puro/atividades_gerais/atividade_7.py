#entrada de dados: nome
nome = input("Qual seu nome? ")
#entrada de dados: ano
ano = input("Qual o ano de nascimento? ")
#subtraindo a diferença, converte a entrada ano em INT
diferenca = 2025 - int(ano)

#Printa na tela o texto com as variáveis
print(f"Olá {nome}, você fará {diferenca} até o final de 2025")