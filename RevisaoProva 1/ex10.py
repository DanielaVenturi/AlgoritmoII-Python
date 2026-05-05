from datetime import date

ano = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - ano

print(f"Idade: {idade}")