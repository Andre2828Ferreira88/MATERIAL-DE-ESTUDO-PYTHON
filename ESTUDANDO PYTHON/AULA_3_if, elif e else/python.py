#if → "se" (testa uma condição).
#elif → "senão se" (testa outra condição se a primeira não for verdadeira).
#else → "senão" (executa se nenhuma das condições anteriores for verdadeira).

idade = 19
if idade >=18:
    print("Pode dirigir")
elif idade >=16:
    print("Pode votar, mas nao pode dirigir")
else:
    print("Ainda é uma criança")