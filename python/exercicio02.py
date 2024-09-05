nome = input("Insira seu nome completo: ")
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) /2
print("Sua média é: ", media)

if media >=7:
    print("Aprovado")
elif media <7:
     print("Reprovado")
