#📝 Exercícios do Dia 4
#1️⃣ Contagem com for

#Imprima os números de 1 a 10.

contador = 1
while contador <= 10:
    print("Contador", contador)
    contador += 1
    
#####################################################


#2️⃣ Tabuada com for

#Peça um número ao usuário e mostre a tabuada dele de 1 a 10.
#Exemplo (usuário digitou 5):

tabuada = int(input("Tabuada do numero: "))
for n in range (11):
    print(f"{tabuada} x {n} = ", tabuada * n)
    
#######################################################

#3️⃣ Soma com while

#Peça números ao usuário até ele digitar 0.
#No final, mostre a soma de todos os números digitados.

soma = 0
while True:
    num = int(input("Digite os numeros de soma até o '0': "))
    if num == 0:
        break
    soma += num
print(" A soma total dos nuemros é ", soma)

#######################################################

#4️⃣ Jogo do número secreto 🎲

#O computador escolhe um número de 1 a 10 (use import random).
#O usuário tem que adivinhar até acertar.
#Cada vez que errar, mostrar se o número é maior ou menor.

import random    
    
numero_secreto = random.randint(1,100)

print("Bem vindo ao jogo da adivinhação")

while True:
    palpite = int(input("Tente acertar o numero: "))

    if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
    elif palpite > numero_secreto:
            print("Tente um número menor.")
    else:
            print("Tente um número maior.")


