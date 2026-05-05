salario = float(input("Digite seu salário: "))

if salario > 5000:
    desconto = salario * 0.10
else:
    desconto = salario * 0.05

print("Desconto:", desconto)