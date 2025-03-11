import os 

os.system("cls")

print("----------CALCULADORA----------")
print("\nADIÇÃO: + ")
print("SUBTRAÇÃO: -")
print("MULTIPLICAÇÃO: *")
print("DIVISÃO: /")

numero1 = float(input("\nDigite o primeiro número:"))
numero2 = float(input("Digite o segundo numero:"))
operacao = input("Digite a operação que deseja:")

if(operacao == "+"):
    resultado = numero1 + numero2
elif(operacao == "-"):
    resultado = numero1 - numero2
elif(operacao == "*"):
    resultado = numero1 * numero2 
elif(operacao == "/"):
    resultado = numero1 / numero2

print("\nOperação escolhida:", operacao)
print("RESULTADO:", resultado )