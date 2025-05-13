def contar_vogais(texto):
    contador = 0
    for letra in texto.lower():
        if letra in "aeiou":
            contador += 1
    return contador

texto = input("digite um texto: ")
quantidade_vogais = contar_vogais(texto)
print(f"o texto possui {quantidade_vogais} vogais")