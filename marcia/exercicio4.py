def calcular_fatorial(num):

    if num < 0:
        return "numero invalido"
    if num == 0 or num == 1:
        return 1
    fatorial = 1
    for i in range(2, num + 1):
        fatorial *= i
    return fatorial

numero = int(input("digite um num inteiro: "))
resultado = calcular_fatorial(numero)
print(f"o fatorial de {numero} é {resultado}.")

