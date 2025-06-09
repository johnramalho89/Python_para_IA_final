entrada = int(input('Coloque sua nota: '))

if entrada < 0:
    print("Impossível!")

elif entrada > 0 and entrada < 49:
    print("Falhar")

elif entrada >= 50 and entrada < 59:
    print("1")
elif entrada >= 60 and entrada < 69:
    print("2")
elif entrada >= 70 and entrada < 79:
    print("3")
elif entrada >= 80 and entrada < 89:
    print("4")
elif entrada >= 90 and entrada < 10:
    print("5")
elif entrada > 100:
    print("Impossível")