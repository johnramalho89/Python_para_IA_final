lista1 = [0,5,3,4,6,8,7,9]
lista2 = [3,8,7,4,6,8,7,9]
resultado = []

def lista_soma(lista1, lista2):    
    for i in range(len(lista1)):
        soma = lista1[i] + lista2[i]
        resultado.append(soma)
    return resultado

print(lista_soma(lista1,lista2))