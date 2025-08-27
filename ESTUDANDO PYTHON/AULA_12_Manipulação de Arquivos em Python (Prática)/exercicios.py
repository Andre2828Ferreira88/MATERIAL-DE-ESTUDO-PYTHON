# 5️⃣ Exercícios do Dia 12

# 1. Criando um diário 📓
# Peça para o usuário escrever uma frase.
# Salve no arquivo diario.txt usando "a" (append).
# Assim, cada execução adiciona uma nova linha no diário.

import datetime

with open("Diario.txt", "a") as f:
    Diario = input("Digite aqui tudo oque voce quer colocar no diario: \n")
    data_atual = datetime.date.today().strftime("%d/%m/%Y")
    f.write(f"{data_atual} : {Diario}\n")
# 2. Lendo o diário 📖
# Abra o arquivo diario.txt e mostre todas as entradas na tela.
with open("Diario.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

# 3. Contando linhas
# Abra o diario.txt.
# Conte quantas linhas (entradas) o arquivo tem e mostre:
# "Você já escreveu X dias no diário."

with open("Diario.txt", "r") as f:
    linhas = sum(1 for linha in f)
    print(f"Voce ja escreveu {linhas} dias no diario") 

# 4. Desafio: Procurando palavras 🔍
# Abra o diario.txt.
# Peça uma palavra ao usuário.
# Mostre em quais linhas essa palavra aparece.

    with open("Diario.txt", "r") as f: 
        palavra  = input("Digite a palavra que voce esta procurando aqui:\n ").lower()
        linhas = f.readlines()
        resultados = [(i + 1, linha.strip()) for i, linha in enumerate(linhas) if palavra in linha.lower()]
        if resultados:
            print(f"palavra ({palavra}) esta na seguintes linhas: ")
            for linha in resultados:
                print(f"Linha {linha[0]}: {linha[1]}")
        else:
            print(f"A palvra ({palavra}) nao foi encontrada no seu Diario.")
    