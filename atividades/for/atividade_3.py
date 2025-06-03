numeros = [10,10,-80]

def Soma_Positivos(lista):
    soma = 0
    for numero in lista:
        if numero > 0:
            soma += numero
    return soma

print(Soma_Positivos(numeros))