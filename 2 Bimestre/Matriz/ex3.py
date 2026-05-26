
matriz = [
    [1, 2],
    [3, 4]
]

soma = 0

for linha in matriz:
    for valor in linha:
        soma += valor

print("Soma dos elementos:", soma)