#4️⃣ Exercícios do Dia 2

#Crie uma lista com 5 nomes de amigos.
#Adicione mais 2 nomes.
#Remova 1 nome.
#Ordene a lista.
#Imprima o resultado final.

#Crie uma tupla com 3 coordenadas de lugares (ex.: casa, escola, trabalho) e imprima cada uma.

#Crie um dicionário com as informações:
#Nome, idade, cidade, altura.
#Adicione a chave "profissão" e um valor.
#Imprima cada chave e valor no formato: chave: valor.

amigos = ["André", "Jefferson", "Galego", "Caue", "Giovanna"]
amigos.append("Diogo")
amigos.append("Machado")
amigos.append("Zion")

amigos.remove("André")

amigos.sort()

print(amigos)


#criando Tuplas

coordenadas = (
    (2234.432 , 12.34), #casa
    (213.32 , 34334.43), #faculdade
    (122.23 , 123.32) #trabalho
)

pessoa = {
    "nome":"André",
    "idade": 19,
    "cidade": "osasco",
    "Altura": 1.79
}
pessoa['Profissão'] = "Jovem Aprendiz"

for chave , valor in pessoa.items():
    print(f"{chave}:{valor}")