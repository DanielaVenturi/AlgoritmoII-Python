n1 = float(input("Digite o primeiro número: "))
op = input("operação (+, -, *, /): ")
n2 = float(input("Digite o segundo número: "))


if op == "+":
    print("Resultado:", n1 + n2)
elif op == "-":
    print("Resultado:", n1 - n2)
elif op == "*":
    print("Resultado:", n1 * n2)
elif op == "/":
    print("Resultado:", n1 / n2)
else:
    print("Operação inválida")