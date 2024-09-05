n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1+n2+n3)/3

if media >=7:
    print(f"PARABÉNS, ALUNO APROVADO : {media}\n")
elif media >=4:
    print(f"O aluno está em RECUPERAÇÃO: {media}\n")
else:
    print(f"Aluno REPROVADO : {media:,.1f}")