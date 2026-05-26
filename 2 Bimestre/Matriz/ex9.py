# Faça busca de valor na matriz.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_procurado = int(input("Digite o valor que deseja buscar: "))

encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):

        if matriz[i][j] == valor_procurado:
            print(f"Valor encontrado na posição [{i}][{j}]")
            encontrado = True

if not encontrado:
    print("Valor não encontrado.")