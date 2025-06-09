import os

# os.remove("dados2.txt")


if os.path.exists("atividades/apagar"):
    print("Sim a pasta existe")
    os.rmdir("atividades/apagar")
else:
    print("Pasta não existe")
    os.mkdir("atividades/Apagar")
    

