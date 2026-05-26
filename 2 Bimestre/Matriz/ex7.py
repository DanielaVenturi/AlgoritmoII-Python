
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for coluna in range(len(matriz[0])):
    soma = 0

    for linha in range(len(matriz)):
        soma += matriz[linha][coluna]

    print(f"Soma da coluna {coluna}: {soma}")