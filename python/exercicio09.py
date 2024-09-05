l = float(input("Quantos litros você colocou? "))
tipo = input("Qual o tipo de combustivel e ou g? " )
valor = 0

if tipo == "g" or tipo == "G":
    valor = l*5.8
    print(f"Voce tem que pagar R${valor:,.2f}: ")
elif tipo == "e" or tipo == "E":
    valor = l*4.9
    print(f"Voce tem que pagar R${valor:,.2f}: ")
else:
    print("Combustivel inválido")









