
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

contador = 0

for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            contador += 1

print("Quantidade de números pares:", contador)