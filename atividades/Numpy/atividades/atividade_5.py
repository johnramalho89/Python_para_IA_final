import numpy as np

def estatisticas_array(array):
    soma = np.sum(array)
    media = np.mean(array)
    return soma, media


meu_array = np.array([10, 20, 30, 40, 50])
print(estatisticas_array(meu_array))