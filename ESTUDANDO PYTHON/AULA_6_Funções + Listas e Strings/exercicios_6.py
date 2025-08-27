#1️⃣ Soma de lista
#Crie uma função soma_lista(lista) que recebe uma lista de números e retorna a soma deles.

def soma_digitos(num):
    return sum(int(digito) for digito in str(num))
num = input("Digite os numeros para se somares: ")
print(f"A soma dos nuemros é : {soma_digitos(num)}")

###########################################################################################
#️⃣ Maior número
#Crie uma função maior_numero(lista) que retorna o maior número de uma lista.

def maior_numero(lista):
    return max(lista)
numeros = [1,2,3,4,5,6,7,8,9,11]
print(maior_numero(numeros))

#############################################################################################
#3️⃣ Palíndromo
#Crie uma função eh_palindromo(palavra) que retorna True se a palavra for igual de trás para frente.
#Exemplo: "arara" → True, "python" → Fal

def eh_palindromo(palavra):
    return palavra.lower() == palavra.lower()[::-1]

print(eh_palindromo('arara')) # true
print(eh_palindromo('python')) # false

#################################################################################################
#4️⃣ Contador de vogais
#Crie uma função conta_vogais(texto) que recebe uma string e retorna quantas vogais (a, e, i, o, u) ela tem.

texto = input("Digite um texto: ")
def conta_vogais(texto):
    vogais = 'aeiou'
    return sum( 1 for char in texto.lower() if char in vogais)

print(conta_vogais("texto"))

##################################################################################################

#5️⃣ Desafio
#Crie uma função estatisticas_texto(texto) que retorna:
#número de caracteres (sem espaços),
#número de palavras,
#a palavra mais longa.



def estatisticas_texto(texto):
    texto_limpo = texto.replace(" ","").replace(".","").replace("!","").replace("?","")
    num_caracteres = len(texto_limpo)
    
    palavras = texto.split()
    num_palavras = len(palavras)
    palavras_mais_longa = max(palavras, key=len)
    
    return {
        "Caracteres": num_caracteres,
        "Palavras": num_palavras,
        "Palavra_mais_longa": palavras_mais_longa
    }
    
resultado = estatisticas_texto("Python é bizzaro")
print(resultado)

