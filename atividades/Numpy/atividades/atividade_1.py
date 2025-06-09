import numpy as np

#Cria a função que recebe uma lista como parametro
def criar_array(lista):
    #np.array converte a lista em array
    return np.array(lista)
#The list
numeros = [1, 2, 3, 4, 5]

#printa e invoca a função passando a lista como argumento
print(criar_array(numeros))