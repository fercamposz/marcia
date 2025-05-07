def mediaa(num1, num2, num3):
    media = (num1 + num2 + num3)/2
    return media

num1 = float(input("Digite seu 1 numero: "))
num2 = float(input("Digite seu 2 numero: "))
num3 = float(input("Digite seu 3 numero: "))

res = mediaa(num1, num2, num3)

print(f"a media é {res}")