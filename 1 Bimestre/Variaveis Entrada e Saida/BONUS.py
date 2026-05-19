nome = input("Digite o seu nome: ")
cidade = input("Digite sua cidade: ")
anoNascimento = int(input("Digite seu ano de nascimento: "))

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: ") or 0)

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * 1.8 + 32
media = (nota1 + nota2 + nota3) / 3
idade = 2026 - anoNascimento

print("\n===== RESULTADOS =====")
print(f"Nome: {nome}")
print(f"Cidade: {cidade}")
print(f"Idade: {idade} anos")

print("---------------------")
print(f"Média: {media}")

print("---------------------")
print(f"{celsius}°C = {fahrenheit}°F")
print("=====================")