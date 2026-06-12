comparacoes = 0

lista = [5, 3, 8, 1]

for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        comparacoes += 1

        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("Lista ordenada:", lista)
print("Comparações:", comparacoes)