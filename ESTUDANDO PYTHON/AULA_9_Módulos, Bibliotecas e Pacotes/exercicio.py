#📝 Exercícios do Dia 9

#1️⃣ Math
#Peça ao usuário um número e mostre:
#raiz quadrada,
#potência ao quadrado,
#valor de seno (math.sin).

import math 
Usuario = int(input("Digite o numero que voce quer saber a raiz: "))
print(f"A raiz quadrada do numero {Usuario} é : ", math.sqrt(Usuario))
print(f"O potencia ao quadradro do {Usuario} é: ", math.pow(Usuario, 2))
print(f"Agora por ultimo o valor so seno é: ", math.sin(Usuario))

#2️⃣ Random
#Faça um sorteio de nomes de uma lista de amigos usando random.choice.
import random
nome_um = input("Digite o primeiro nome do sorteio: ")
nome_dois = input("Digite o segundo nome do sorteio: ")
nome_tres = input("Digite o terceiro nome do sorteio: ")

print(random.choice([nome_um, nome_dois, nome_tres]))
#3️⃣ Datetime
#Mostre a data e hora atual. Depois mostre apenas o ano de nascimento de uma pessoa que informou a idade.
from datetime import datetime
agora = datetime.now()
pessoa = int(input("Digite sua idade, direi que ano voce nasceu: "))
print("O ano que voce nasceu foi: ", agora.year - pessoa)
print(f"Data e hora atual: {agora}")

#4️⃣ Desafio: Jogo de Dados 🎲
#Simule um jogo de 2 dados: cada jogador rola 1 dado (random.randint(1,6)).
#Quem tirar o maior número vence.

import random
enter = input("De um ENTER para jogar os dois dados: ")

dadoUm = random.randint(1,10)
dadoDois = random.randint(1,10)

soma = (dadoUm + dadoDois)

print(f"O dado um deu {dadoUm}, o dado dois deu {dadoDois}. Resultando em : {soma}")
