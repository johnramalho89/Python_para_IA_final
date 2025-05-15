salario_hora = float(input("Digite o salário por hora: "))
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
dia_semana = input("Digite o dia da semana: ")

if dia_semana == "domingo":
    salario_dia = (salario_hora * 2) * horas_trabalhadas
else:
    salario_dia = salario_hora * horas_trabalhadas
    
print(f"Salário diário: R$ {salario_dia:.2f}")