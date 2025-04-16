import random
import time

numeros = list(range(1, 76))
random.shuffle(numeros)

print(" BINGO DA MÁRCIA ")
print("começando o sorteio")

input("Aperta Enter pra sortear o primeiro número!")

while len(numeros) > 0:
    input("aperta enter...")
    numero = numeros.pop(0)

    if numero >= 1 and numero <= 15:
        letra = "B"
    elif numero >= 16 and numero <= 30:
        letra = "I"
    elif numero >= 31 and numero <= 45:
        letra = "N"
    elif numero >= 46 and numero <= 60:
        letra = "G"
    else:
        letra = "O"

    print(f" a boa é {letra}-{numero}")

print("n foi dessa vez")
