
import re
while True:
    senha = input("Digite uma senha: ")
    temMaiuscula = re.search("[A-Z]",senha)
    temMinuscula = re.search("[a-z]",senha)
    temNumero = re.search("[0-9]",senha)
    if len(senha) < 8:
        print("Senha Precisa ter 8 Caracteres")
   
    elif temMaiuscula == None:
        print(" 1 Letra maiúscula")
        
    elif temMinuscula == None:
        print(" 1 Letra minúscula")
        
    elif temNumero == None:
        print(" 1 número")

    else:
        print("Senha compatível")
        break

        
