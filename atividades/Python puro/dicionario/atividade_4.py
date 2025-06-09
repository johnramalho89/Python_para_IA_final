banco_filmes = []

def add_filme(database, nome, diretor, ano, duracao):
    filme = {
        "nome": nome,
        "diretor": diretor,
        "ano": ano,
        "tempo de execução": duracao
    }
    database.append(filme)
    print(banco_filmes)
    
while True:
    nome = input('Nome do filme: ')
    diretor = input('NOme do diretor: ')
    ano = int(input('ano do filme: '))
    duracao = int(input('Duração: '))
    add_filme(banco_filmes, nome, diretor, ano, duracao)
    

    
