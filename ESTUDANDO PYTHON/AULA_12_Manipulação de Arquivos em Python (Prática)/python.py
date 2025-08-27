# 1️⃣ Criando e escrevendo em arquivos
# O modo "w" cria o arquivo se não existir (ou apaga e recria se já existir)

with open("exemplo.txt", "w") as f:
    f.write("Olá, mundo!\n")
    f.write("Segunda linha de texto. \n")

# Iniciando o codigo voce cria um arquivo .TXT

# 2️⃣ Lendo arquivos

with open("exemplo.txt", "r") as f:
    conteudo = f.read()
    print("Conteúdo do arquivo:\n", conteudo)
    
# 3️⃣ Lendo linha por linha

with open("exemplo.txt", "r") as f:
    for linha in f:
        print("linha", linha.strip()) #strip remove o \n
        
# 4️⃣ Adicionando conteúdo sem apagar
# O modo "a" adiciona conteúdo no final do arquivo:

with open('exemplo.txt', "a") as f:
    f.write("Nova linha adicionada!\n")