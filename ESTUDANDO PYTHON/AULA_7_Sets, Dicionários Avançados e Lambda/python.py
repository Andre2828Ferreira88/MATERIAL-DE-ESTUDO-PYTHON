#🔹 1. Sets (Conjuntos)
#Um set é como uma lista, mas:
#Não tem ordem
#Não aceita elementos repetidos

frutas = {"maçã", "banana", "laranja", "maçã"}
print(frutas) # {'maçã', 'banana', 'laranja'} → a maçã repetida sumiu

#Outras opções

A = {1,2,3,4}
B = {3,4,5,6}

print(A | B ) # união: {1,2,3,4,5,6}
print(A & B)  # interseção: {3,4}
print(A - B)  # diferença: {1,2}

#🔹 2. Dicionários Avançados

#Já usamos dicionário, 
#mas agora vamos manipular mais fundo.

aluno = {
    "nome": "André",
    "idade" : 19,
    "notas" : [7.5 , 8.0 , 9.2]
}

print(aluno['nome'])
print(sum(aluno['notas']) / len(aluno["notas"])) #media

# 🔹 3. Funções Lambda
# Uma lambda é uma função pequena em uma linha só.

dobro = lambda x: x * 2
print(dobro(5)) #10

3##################################################################
# Usada muito com map, filter e sorted:

numeros = [1,2,3,4,5]

dobrados = list(map(lambda x: x*2, numeros))
print(dobrados) # [2,4,6,8,10]

pares = list(filter(lambda x: x%2 == 0, numeros))
print(pares) #[2,4]

nomes = ['andre', 'jefferson', 'galego']
ordenados = sorted(nomes, key=lambda nome: len(nome))
print(ordenados) # ['andre', 'galego', 'Jefferson']