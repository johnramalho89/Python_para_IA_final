""" palavra1 = "ex"
palavra2 = "emplo"
palavraCompleta = palavra1 + palavra2

print(palavraCompleta * 5) 

print("2" * len(palavraCompleta)) """

entrada = input("Digite um texto': ")

Penultimo = len(entrada) - 2

if entrada[Penultimo] == entrada[1]:
    print(f"São iguais letra 1: {entrada[Penultimo]} e o letra 2:  {entrada[1]} ")
    
else:
    print(f"Não são iguais letra 1: {entrada[Penultimo]} e o letra 2:  {entrada[1]} ")
