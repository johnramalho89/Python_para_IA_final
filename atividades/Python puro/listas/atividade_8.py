import re

def cadastrar_senhas():
    senhas = []
    #aqui é while de repetição
    while len(senhas) < 5:
        senha = input(f"Digite a {len(senhas)+1}ª senha: ")

        if len(senha) >= 8 and re.search("[0-9]",senha) != None:
            senhas.append(senha)
        else:
            print("Senha inválida! Deve ter pelo menos 8 caracteres E conter um número.")

    print("Senhas válidas:")
    
    i = 0
    while i < len(senhas):
        print(senhas[i])
        i += 1
        
cadastrar_senhas()