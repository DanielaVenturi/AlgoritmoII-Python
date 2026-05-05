valor_hora = float(input("Digite o valor da hora: "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))

salario = valor_hora * horas
desconto = salario * 0.11
salario_liquido = salario - desconto

print(f"Salário bruto: R$ {salario:.2f}")
print(f"Desconto INSS: R$ {desconto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")