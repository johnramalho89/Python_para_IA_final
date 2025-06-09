import numpy as np

def somar_matrizes(matriz1, matriz2):
    if np.shape(matriz1) == np.shape(matriz2):
        return matriz1 + matriz2
    else:
        return "Erro: As matrizes devem ter o mesmo tamanho."
    
m1 = np.array([[1, 2], [3, 4],[5,6]])
m2 = np.array([[5, 6], [7, 8]])

print(somar_matrizes(m1,m2))
