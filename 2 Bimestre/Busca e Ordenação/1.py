def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

lista = [4, 7, 2, 9, 1, 5]

valor = int(input("Digite o valor a buscar: "))

resultado = busca_linear(lista, valor)

print("Índice:", resultado)