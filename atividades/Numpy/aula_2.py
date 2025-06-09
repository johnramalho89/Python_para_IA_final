import numpy as np

#aqui é uma variavel que representa o método default_rng
rng = np.random.default_rng()


#Criar Array apartir de listas e tuplas
lista_py = [1,2,3,4,5,6]
print(lista_py)
array_1d = np.array(lista_py)
print(array_1d)

#np.array converte tuplas e listas em array (arranjo)
lista2_py = [[1,2,3,4],[1,2,3,4]]
array_2d = np.array(lista2_py)

print(array_2d)
tupla = (1,2,3,4,5,6,7,8,9,10)
array_tupla = np.array(tupla)
print(array_tupla)

#np.zeros
#cria um array preenchido por zeros
zero_array = np.zeros((3,3),int)
print(f"Array de zero:\n {zero_array}")

#np.ones
one_array = np.ones((2,3),int)
print(one_array)

#no.pfull
#cria um array preenchido com números especificos
full_array = np.full((2,4),7.5)
print(full_array)

#np arrange
array_arrange = np.arange(0,10,2)
print(array_arrange)

array_float_arange = np.arange(0.0,1.0,0.25)
print(array_float_arange)

#array de números aleatórios
array_aleatorios = rng.random((2,5))
array_aleatorios2 = rng.integers(0, 1000, size=10)

print(array_aleatorios)
print(array_aleatorios2)

#ìndices em Numpy
#indice vetor
array_indice = np.array([1,2,5,9,8])
print(f"elemento 0: {array_indice[0]}")
print(f"elemento 3: {array_indice[3]}")

#indice Matriz
array_indice2 = np.array([[1,2,5,9,8],[5,9,8,7,6]])
print(f"Elemento na linha 0, coluna 2: {array_indice2[0,2]}")

#Slicing
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 12, 13],
                  [14, 7, 15, 16]])

fatia2d_a = arr2d[:3, 1:3]
print(fatia2d_a)
# Saída:
# [[2 3]
#  [6 7]]

#Operações matemáticas
#adição
array_a = np.array([1,3,5,8])
array_b = np.array([2,3,4,5])

soma = array_a + array_b
print(soma)

#subtração
menos = array_a - array_b
print(menos)

#multiplicação
vezes = array_a * array_b
print(vezes)

#divisão
divisao = array_a / array_b
print(divisao)

#Copy e View
precos = np.array([180.00,10.99,20.50])
print(f"preços: {precos}")

precoAjustado = precos
print(precos[0] * 2)

#copy, faz uma cópia de outra, qualquer alteração na copia, não altera a original
PrecoAjustado2 = precos.copy()

#Iteração
array = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9,  1, 25, 35])

for n in array:
    print(f"Valor:{n} ")










