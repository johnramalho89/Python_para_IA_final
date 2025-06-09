#Criar uma lista
minha_lista = [10,30,15]

#Acessando elementos por índice
print(minha_lista[1])
print(minha_lista[2])


#Trabalhando com elementos da lista
resultado = minha_lista[0] + minha_lista[2]
print(resultado)

#tamanho da lista
tamanho_lista = len(minha_lista)
print(f"Minha Lista tem {tamanho_lista} de tamanho")

#fatiar listas
letras = ['a','b','c','d','e','f']
print(letras[1:4]) # ele corta de 1 ao elmento de indice 4
print(letras[:3]) #corta do início até o 3-1
print(letras[3:]) #do índice 3 até o final
print(letras[::2]) # todos, com passo 2
print(letras[::-1]) # lista invertida

#Adicionar itens a lista
numeros = [10,50,36,25,14]


#adicionar itens em lugar específico
numeros.insert(1,50)
numeros.insert(0,20)
numeros.insert(7,200)


#Remove itens pelo indice
numeros.pop(2)
numero_deletado = numeros.pop(0)


#Remove o valor de um elmento de uma lista
numeros.remove(50)
numeros.insert(10,"John")

numeros.remove("John")

#Sort - Classificação
lista = [0,45,68,98,78,65,23,35,54,47,89]
lista.sort()
#Sorted cria uma cópia da lista original em outra variavel
lista_v2 = sorted(lista)

print(lista_v2)
print(lista)

#Máximo. mínimo e a soma
Lista_numeros = [0,45,78,6,32,15]
print(max(Lista_numeros))
print(min(Lista_numeros))
print(sum(Lista_numeros))

lista_mediana = [15,48,79,36,56,89,74,15,32,41,50,3,1,10,89,90,95]

def mediana(minha_lista: list):
    ordenada = sorted(minha_lista)
    centro_lista = len(ordenada) // 2
    print(ordenada)
    return ordenada[centro_lista]

print(f"A mediana é {mediana(lista_mediana)}")

    


