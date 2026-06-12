def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

lista = [1, 3, 5, 7, 9, 11, 13]

print("Busca Linear:", busca_linear(lista, 11))
print("Busca Binária:", busca_binaria(lista, 11))