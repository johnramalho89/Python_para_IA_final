""" def quadradoString(texto, tamanho):
    total_caracteres = tamanho * tamanho
    repetida = (texto * ((total_caracteres // len(texto)) + 1))[:total_caracteres]
    i = 0
    while i < total_caracteres:
        print(repetida[i:i+tamanho])
        i += tamanho
        
        
quadradoString("John",10) """

# Definir a função 
def Repetir(palavra, numero):
    #Variavel que multiplica a string pelo numero passado como parametro
    stringTotal = palavra * numero
    # variavel que inicia em zero para posterioemnte ser usado como controle
    linha = 0
    while linha < numero:
        coluna = 0
        letras = " "
        while coluna < numero:
            posicao = linha * numero + coluna
            letras += stringTotal[posicao]
            coluna += 1
        print(letras)
        linha += 1

Repetir("Jumanji",10)