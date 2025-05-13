def contagem_regressiva(n):
    if n <= 0:
        print("fim")
    else:
        print(n)
        contagem_regressiva(n - 1)

n = int(input("digita seu numero: "))
contagem_regressiva(n)
