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

lista = [8, 3, 1, 9, 5]

lista.sort()

print("Lista ordenada:", lista)

valor = int(input("Digite o valor para buscar: "))

print("Índice:", busca_binaria(lista, valor))