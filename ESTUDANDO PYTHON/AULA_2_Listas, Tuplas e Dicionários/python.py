#Lista mutavel
frutas = ["maçã", "banana", "uva"]

frutas.append("laranja")

print(frutas)

#Principais métodos:
#
#.append(x) → adiciona no final
#
#.insert(i, x) → adiciona na posição i
#
#.remove(x) → remove a primeira ocorrência
#
#.pop(i) → remove pelo índice (padrão último)
#
#.sort() → ordena
#
#.reverse() → inverte


#Estrutura imutavel (Tuplas)
coordenadas = (23.5 , 46.6)
print(coordenadas[0])



#Criar um dicionario 
pessoa = {
    "nome":"André",
    "idade": 19,
    "cidade": "Osasco"
    
}

pessoa["Altura"] = 1.78
print(pessoa)
