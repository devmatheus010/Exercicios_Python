nome = input("Qual seu nome: ")
idade = input("Qual sua idade: ")
salario = float(input("Qual seu salario: "))

novoSal = (salario * 0.1) + salario
print("Seu nome é: ", nome)
print("Sua idade é: ", idade)
print(f"Seu salario é : {novoSal:, .2f}")