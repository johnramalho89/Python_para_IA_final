lista_estrela = [3,7,11,2]


def estrelasCaracter (lista: list):
    for i in lista:
        estrelas = "*" * i
        print(estrelas)
        
estrelasCaracter(lista_estrela)