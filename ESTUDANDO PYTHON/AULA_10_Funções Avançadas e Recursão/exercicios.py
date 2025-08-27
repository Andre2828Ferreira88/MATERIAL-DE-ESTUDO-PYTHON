# 📝 Exercícios do Dia 10

# 1️⃣ Crie uma função boas_vindas que tenha um parâmetro nome com valor padrão "Visitante".
# Mostre na tela "Bem-vindo(a), <nome>".

def saudacao(nome = "Visitante"):
    print(f"Olá, {nome}!")
    
    

# 2️⃣ Crie uma função media que aceite qualquer quantidade de números 
# (com *args) e retorne a média.

def soma(*args):
    return sum(args)
print(soma(1,2,3,4,5) / 2)


# 3️⃣ Crie uma função aluno_info que aceite dados nomeados (**kwargs) como nome, idade e curso.
# Mostre todos os valores.

def exebir_infos(**kwargs): #receber valores nomeados (dicionarios)
    for chave, valor in kwargs.items():
        print(f"{chave}: {chave}")
        
exebir_infos(nome="André", idade=19, curso= 'ADS')


# 4️⃣ Faça uma função recursiva que calcule a soma dos números de 1 até n.
# Exemplo: soma_recursiva(5) = 15.

def soma_recursiva(n):
    if n == 1:
        return 1
    return n + soma_recursiva(n - 1)

print(soma_recursiva(5))  # 15
print(soma_recursiva(10)) # 55


# 5️⃣ 🔥 Desafio:
# Faça uma função recursiva que calcule o n-ésimo termo da sequência de Fibonacci:
# 0, 1, 1, 2, 3, 5, 8, ...
# Exemplo: fibonacci(6) = 8.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
print(fibonacci(10)) # 55