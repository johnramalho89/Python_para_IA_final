pin_correto = "4321"
tentativas = 0

while True:
    pin = input("Digite o código PIN: ")
    if pin == pin_correto:
        print(f"PIN correto! Você errou {tentativas} vez(es) antes de acertar.")
        break
    else:
        print("PIN incorreto. Tente novamente.")
        tentativas += 1