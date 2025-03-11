import os
 
os.system("cls")
 
print("--------SALÁRIO--------")
 
nome = input("Digite o nome do professor(a): ")
nivel = int(input("Digite o nível do professor: "))
aulas = int(input("Digite a quantidade de aulas lecionadas: "))
 
if(nivel == 1):
    salario = aulas * 12
    print("O professor(a) receberá R$")
elif(nivel == 2):
    salario = aulas * 17
    print("O professor(a) receberá R$")
elif(nivel == 3):
    salario = aulas * 25
    print("O professor(a) receberá R$")
 
print("====================================================")
 
print("Nome do professor(a) ", nome)
print("Nível do professor: ", nivel)
print("Quantidade de aulas lecionadas: ", aulas)
print("Salário que o professor(a) ira receber: R$", salario)
 