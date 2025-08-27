#📝 Exercícios do Dia 5

#1️⃣ Crie uma função boas_vindas(nome) que recebe um nome e imprime:
#Olá, [nome], seja bem-vindo!

nome = input("Qual o seu nome: ")

def BoasVindas(nome):
    print(f"Olá {nome}, seja bem vindo!")
    
BoasVindas(nome)

#####################################################################
#2️⃣ Crie uma função dobro(numero) que retorna o dobro de um número.
#Exemplo: dobro(4) → 8.

N = int(input("Digite o numero que voce quer dobrar: "))

def Dobro(N):
    return N+N
resuldo = Dobro(N)
print(f" A dobras de {N} é {resuldo}")
Dobro(N)


#####################################################################
#3️⃣ Crie uma função media(n1, n2, n3) que calcula
# a média de 3 números e retorna o resultado.
#Se a média for ≥ 7, retorne "Aprovado ✅".
#Se entre 5 e 6.9 → "Recuperação ⚠️".
#Se < 5 → "Reprovado ❌".





def Media():
    
    n1 = float(input("Digite a nota da primeira prova: "))
    n2 = float(input("Digite a nota da Segunda prova: "))
    n3 = float(input("Digite a nota da Terceira prova: "))
    
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        return (f"Aprovado : {media:2f}")
    elif media >= 5:
        return (f"Recuperação: {media:2f}")
    else:
        return(f"reprovado: {media:2f}")

print(Media())


###################################################################
#4️⃣ Crie uma função eh_par(numero) 
# que retorna True se for par e False se for ímpar.
#Depois, peça um número ao usuário e use a função 
# para mostrar a mensagem certa

def eh_par(numero):
    return numero % 2 == 0

n = int(input("Digite o numero no qual voce quer saber se é par: "))
if eh_par(n):
        print("Seu numero é par")
else:
        print("Seu numero é ímpar")


######################################################################

#5️⃣ Desafio: transforme o jogo do número secreto do Dia 4
#em uma função chamada jogo().
#Assim você pode rodar o jogo só chamando:

def Jogo():
    import random
    
    numero_secreto = random.randint(1,100)
    
    print("Bem vindo ao jogo da adivinhação")
    
    while True:
        palpite = int(input("Tente acertar o numero: "))
        if palpite == numero_secreto:
            print("Parabens! Acertou.")
            break
        elif palpite > numero_secreto:
            print("Tente um numero menor.")
        else:
            print("Tente um numero maior ")    
            
Jogo()  



    