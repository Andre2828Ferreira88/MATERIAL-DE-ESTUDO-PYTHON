#🔑 Como abrir arquivos

open("nome_arquivo.txt", "modo")

# "r" → leitura (read)
# "w" → escrita (write) – apaga o conteúdo anterior
# "a" → append – adiciona no final sem apagar o que já existe

# 🔑 Melhor forma (boa prática)

with open("Arquivo.txt", "r") as f:
    conteudo = f.read()
    
# O with garante que o arquivo será fechado automaticamente, sem precisar f.close().

# 🔑 Métodos principais
# f.write("texto") → escreve uma string no arquivo.
# f.writelines(lista) → escreve uma lista de strings.
# f.read() → lê todo o conteúdo como uma única string.
# f.readline() → lê apenas uma linha.
# f.readlines() → retorna todas as linhas em uma lista.