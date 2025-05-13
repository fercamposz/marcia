def converter(c):
    return c * 1.8 + 32
ce = float(input("digite a temperatura em Celsius: "))
f = converter(ce)
print(f"{ce}°C é igual a {f:.2f}°F")