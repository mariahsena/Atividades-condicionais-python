import os
 
os.system("cls")
 
print("--------DESCONTO--------")
 
produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade de produto(s): "))
valor = float(input("Digite o valor do produto(s): "))
 
sem_desconto = quantidade * valor
 
if(quantidade <= 5):
    desconto = (( 2 / 100) * valor)
    com_desconto = valor - desconto
    total = quantidade * com_desconto
    print("Com desconto o valor fica ", com_desconto)
elif(quantidade >5 and quantidade <=10):
    desconto = ((3 / 100) * valor)
    com_desconto = valor - desconto
    total = quantidade * com_desconto
    print("Com desconto o valor fica ", com_desconto)
elif(quantidade >10):
    desconto = ((5 / 100) * valor)
    com_desconto = valor - desconto
    total = quantidade * com_desconto
    print("Com desconto o valor fica ", com_desconto)
 
 
print("====================================================")
 
print("Nome do produto: ", produto)
print("Quantidade de produto: ", quantidade)
print("Preço unitário: ", valor)
print("Preço sem desconto: ", sem_desconto)
print("Preço com desconto: ", total)