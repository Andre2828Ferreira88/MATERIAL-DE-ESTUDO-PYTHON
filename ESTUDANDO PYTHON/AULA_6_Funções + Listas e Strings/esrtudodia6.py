#🔹 Revisando Listas em funções
#Você pode passar uma lista como parâmetro de função e trabalhar nela.

def soma_lista(numeros):
    return sum(numeros)
print(soma_lista([1,2,3,4,5]))



##########################################################################

texto = "Pyhton é showwww"

print(texto.lower()) #tudo minusculos
print(texto.upper()) # tudo maisculo
print(texto.strip()) # Remove os espaçoes extras
print(texto.replace('Pyhton é showwww', 'Java')) # troca palavras
print(len(texto)) # tamanho da string
print(texto.split()) # quebra em lista ["Python", "é", "incrível!"]
