import numpy as np

def gerar_array_intervalo(inicio, fim):
    if inicio <= fim:
        return np.arange(inicio, fim + 1)

print(gerar_array_intervalo(3, 7))