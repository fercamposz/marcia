def imc(peso, altura):
   IMC = peso / altura
   return IMC

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

res = imc(peso, altura)
print(f"Seu imc é de {res:.2f}")
