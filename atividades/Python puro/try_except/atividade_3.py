frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

try:
    indice = int(input("Digite um índice (0 a 4): "))
    print("Fruta selecionada:", frutas[indice])
except IndexError:
    print("Índice fora do alcance.")

except ValueError:
    print("Por favor, digite um número inteiro válido.")
    
