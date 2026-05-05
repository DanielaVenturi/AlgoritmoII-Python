nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))

if idade >= 18 and salario > 2000:
    print(f"{nome}, você pode financiar um carro!")
else:
    print(f"{nome}, você NÃO pode financiar um carro.")