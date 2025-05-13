def maior_n(n):
   maior = None
   for i in range(n):
       numero = int(input(f"digite o {i + 1}º número: "))
       if maior is None or numero > maior:
           maior = numero
   return maior


n = int(input("quantos num vc deseja digitar? "))
resultado = maior_n(n)
print(f"o maior numero entre os {n} números digitados é: {resultado}")