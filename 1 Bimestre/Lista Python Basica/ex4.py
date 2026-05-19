from datetime import date

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

print(f"Você tem {idade} anos")