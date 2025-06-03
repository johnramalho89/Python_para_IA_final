idade = int(input("Qual a sua idade? "))

if idade < 0:
    
    print("Você nem nasceu ainda!")
    
elif idade < 5:
    print("Tão novinho usando computador? Que precoce!")
    
elif idade > 130:
    print("Você é a pessoa mais velha do mundo?!")
    
else:
    print("Idade registrada com sucesso.")
