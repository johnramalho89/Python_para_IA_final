import math

  
while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))

    if numero == 0:
        print("Encerrando o programa.")
        break
    elif numero < 0:
        print("Número inválido.")
    else:
        raiz = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {raiz}")