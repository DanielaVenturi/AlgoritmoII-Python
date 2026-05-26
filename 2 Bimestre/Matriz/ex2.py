matriz = []

for linha in range(2):

    nova_linha = []

    for coluna in range(2):

        valor = int(input(f"Digite um número: "))

        nova_linha.append(valor)

    matriz.append(nova_linha)

for nova_linha in matriz:
    print(nova_linha)  