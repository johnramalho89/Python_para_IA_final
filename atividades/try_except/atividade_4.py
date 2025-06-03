numeros = [10, 20, 30]

try:
    divisor = int(input("Digite um número divisor: "))
    indice = int(input("Digite um índice (0 a 2): "))
    
    resultado = numeros[indice] / divisor
    print(f"Resultado da divisão: {resultado}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

except IndexError:
    print("Erro: Índice fora do alcance da lista.")

except Exception as e:
    print("Erro inesperado:", e)