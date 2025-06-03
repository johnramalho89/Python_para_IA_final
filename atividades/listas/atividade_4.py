notas = []
aprovadas = []
#Enquanto tamanho da lista "notas" for menor que 5 vai repetir o while
while len(notas) < 5:
    #input de entrada do usúario
    nota = int(input("Qual a nota: "))
    #adiciona a nota do imput na lista notas
    notas.append(nota)
    #If que verifica se a nota é maior que 6
    if nota >= 6:
        #adiciona a nota a uma nova lista se a nota for maior que 6
        aprovadas.append(nota)
        
#Ao final do Script, ele exibe as notas aprovadas maior que 6
print(f"Notas aprovadas: {aprovadas}")
    
        

    