#🔹 1. Importando módulos internos

import math
print(math.sqrt(16))
print(math.pi)

#Ou importando só uma função:

from math import sqrt, pi
print(sqrt(25))
print(pi)

#🔹 2. Usando random

import random
print(random.randint(1,10)) #numero aleatorio entre 1 a 10.
print(random.choice(["maça", "banana", "laranja"])) #escolher intens aleaotirios da lista

#🔹 3. Usando datetime

from datetime import datetime

agora = datetime.now()
print("Data e hora atual: ", agora)
print("Ano: ",agora.year)
print("mes: ",agora.month)
print("Dia: ", agora.day)

import requests

respostas = requests.get("https://api.github.com")
print(respostas.status_code)