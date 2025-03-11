import os

os.system("cls")

print("------ CÁLCULO DO IMC------")
nome = input("Digite o seu nome:")
idade = float(input("Digite a sua idade:"))
peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura:"))

imc = peso / (altura * altura)

if(imc <= 16.9 ):
    status = ("Muito baixo do peso")
elif(imc >=17 and imc <=18.4):
    status = ("Abaixo do peso")
elif(imc >=18.5 and imc <=24.9):
    status = ("Peso normal")
elif(imc >=25 and imc <=29.9):
    status = ("Acima do peso")
elif(imc >=30 and imc <=34.9):
    status = ("Obesidade grau I")
elif(imc >=35 and imc <=40):
    status = ("Obesidade grau II")
elif(imc >=40):
    status = ("Obesidade grau III")



print("\n///-------------------------///")
print("\n|Nome da pessoa:", nome )
print("|Idade da pessoa:", idade )
print("|Peso da pessoa:", peso )
print("|Altura da pessoa:", altura )
print("|IMC da pessoa:", imc )
print(status)