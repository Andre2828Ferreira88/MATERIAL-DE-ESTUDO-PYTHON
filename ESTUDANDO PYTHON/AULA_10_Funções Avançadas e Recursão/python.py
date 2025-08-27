#1️⃣ Parâmetros nomeados e valores padrão

#Você pode definir valores padrão nos parâmetros de uma função:

def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")
    
saudacao("Andre")
saudacao()

#2️⃣ Args e Kwargs
#Permitem funções com quantidade variável de argumentos.

def soma(*args): #receber varios valores em forma de tuplas
    return sum(args)

print(soma(1,2,3,4,5)) #15 

def exebir_infos(**kwargs): #receber valores nomeados (dicionarios)
    for chave, valor in kwargs.items():
        print(f"{chave}: {chave}")
        
exebir_infos(nome="André", idade=19, curso= 'ADS')

#3️⃣ Funções dentro de funções (Nested Functions)
#Você pode criar funções dentro de outras funções:
def operacoes(x,y):
    def soma():
        return x + y
    def multiplicacao():
        return x * y
    return soma() + multiplicacao()

print(operacoes(2,3))  # (2+3) + (2*3) 11 
            
            

# 4️⃣ Recursão (quando uma função chama a si mesma)
# Exemplo clássico: fatorial.

def fatorial(n):
    if n == 0 or n == 1: # caso base
        return 1
    else:
        return n * fatorial(n-1)
print(fatorial(5)) # 120
    

