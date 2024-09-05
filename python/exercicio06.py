n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))

if n1 > n2:
    print(f"{n2},{n1}")
elif n1 < n2:
    print(f"{n1}, {n2}")
else:
    print(f"Os numeros {n1} e {n2} são iguais")