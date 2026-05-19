a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")

if b != 0:
    print(f"Divisão: {a / b}")
    print(f"Divisão inteira: {a // b}")
    print(f"Resto: {a % b}")
else:
    print("Não é possível dividir por zero")