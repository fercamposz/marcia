def calcular_troco(valor_compra, valor_pago):
    if valor_pago < valor_compra:
        print("falta dinheiro")
        return 0
    return valor_pago - valor_compra
valor_compra = float(input("digite o valor da compra: "))
valor_pago = float(input("digite o valor pago: "))
troco = calcular_troco(valor_compra, valor_pago)
if troco > 0:
    print(f" seu troco é: R${troco:.2f}")