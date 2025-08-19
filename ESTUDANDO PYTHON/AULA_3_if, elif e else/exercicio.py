#📝 Exercícios do Dia 3
#1️⃣ Maioridade

#Peça a idade do usuário com input().
#Se for 18 ou mais → "Maior de idade".
#Se for entre 13 e 17 → "Adolescente".
#Se for menor → "Criança".

idade= int(input("Digte a sua idade: "))

if idade >= 18:
     print("Maior de idade")
elif idade >= 13:
    if idade <= 17:
        print(" Adoleceste")
else:
    print("Criança")
    
    

#2️⃣ Nota escolar

#Peça uma nota de 0 a 10.
#Se ≥ 7 → "Aprovado ✅".
#Se entre 5 e 6.9 → "Recuperação ⚠️".
#Se < 5 → "Reprovado ❌".

nota = float(input("Qual foi sua nota na prova?: "))

if nota == 10:
    print("PASSOU COM NOTA MAXIMA")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    if nota <=6.9:
        print("Recuperação")
else:
    print("recuperação")
    
    
    
#3️⃣ Par ou ímpar

#Peça um número inteiro.
#Se for par → "O número X é par".
#Se for ímpar → "O número X é ímpar".

Numero = int(input("Digite um numero: "))

if Numero % 2 == 0:
    print(f"{Numero} é par")
else:
    print(f"{Numero} é impar")
    


#4️⃣ Calculadora simples

#Peça 2 números e uma operação (+, -, *, /).
#Use if/elif/else para calcular o resultado.

nUM = float(input("Digite o primeiro numero: "))
nDois = float(input("Digite o segundo numero: "))

Operador = input(" Escolha qual operador voce usara ( + - * /)")

Mais = nUM + nDois
Menos = nUM - nDois
Vezes = nUM * nDois
Divisao = nUM / nDois

if Operador == '+':
    print(f"O Calculo é {Mais}"),
elif Operador == '-':
    print(f"O Calculo é {Menos}"),
elif Operador == '*':
    print(f"O calculo é {Vezes}"),
elif Operador == '/':
    print(f"O calculo é {Divisao}"),
else: 
    print(f"Operador INVALIDO")