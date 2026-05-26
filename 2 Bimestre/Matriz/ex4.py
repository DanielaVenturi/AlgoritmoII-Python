
matriz = [
    [5, 8, 2],
    [1, 9, 4],
    [7, 3, 6]
]

maior = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor

print("Maior valor:", maior)