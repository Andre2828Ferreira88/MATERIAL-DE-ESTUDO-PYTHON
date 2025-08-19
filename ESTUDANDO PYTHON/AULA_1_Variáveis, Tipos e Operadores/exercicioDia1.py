#Crie variáveis para guardar seu nome, idade, altura e cidade.

#Calcule:
#Ano de nascimento
#Idade daqui a 10 anos
#Altura em centímetros

#Crie uma variável pode_dirigir que seja True se tiver 18 anos ou mais, e imprima o resultado.

#Imprima tudo de forma organizada, usando print() e texto descritivo.


nome = "André"
idade = 19
altura = 1.78
cidade = "Osasco"

Ano_De_Nascimento = 2025 - idade
Idade_mais_dez = idade + 10
altura_em_centimentros = altura * 100

pode_dirigir = idade <= 18

print("Ano de nascimento do ", nome , " é ", Ano_De_Nascimento)
print("A Idade de ", nome ," daqui 10 anos será ", Idade_mais_dez)
print("A altura de ", nome , " em centimetros é ", altura_em_centimentros)
print(nome, " esta permitido a dirigir? : ", pode_dirigir)