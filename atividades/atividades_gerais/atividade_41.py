senha_correta = input("Crie uma senha: ")

while True:
    tentativa = input("Digite a senha novamente: ")
    if tentativa == senha_correta:
        print("Senha confirmada com sucesso!")
        break
    else:
        print("Senhas diferentes. Tente novamente.")
