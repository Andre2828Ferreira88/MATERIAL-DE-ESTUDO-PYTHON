# 📝 Exercícios do Dia 7

# 1️⃣ Sets
# Crie dois conjuntos de números {1,2,3,4,5} e {4,5,6,7,8}.
# Mostre: união, interseção e diferença.

conjuntoUM = {1,2,3,4,5}
conjuntoDOIS = {4,5,6,7,8}

print( conjuntoUM | conjuntoDOIS )
print( conjuntoUM & conjuntoDOIS)
print( conjuntoUM - conjuntoDOIS) 

##############################################################
# 2️⃣ Dicionário

# Crie um dicionário com informações de um aluno:
# nome, idade, notas (lista).
# Depois mostre:
# média das notas,
# o maior valor da lista de notas.

aluno = {
    "nome": "Andre Ferreira Monteiro",
    "Idade": 19,
    "turno": "NOTURNO",
    "notas": [8.0,8.0,9.0]
}
print(aluno)
print(sum(aluno["notas"]) / len(aluno["notas"]))
print(max(aluno["notas"]))


#3️⃣ Lambda + map
# Crie uma lista de números e use map com 
# lambda para elevar cada número ao quadrado.

numeros = [ 1,2,3,4,5 ]
dobrados = list(map(lambda n: n *n, numeros))
print(dobrados)


################################################################
#5️⃣ Desafio
# Dada uma lista de nomes, ordene
# pela quantidade de letras usando sorted e lambda.

nomes = ["Andre", "Jefferson", "Caue", "Claes"]
ordenados = sorted(nomes, key=lambda nome: len(nome))
print(ordenados)
