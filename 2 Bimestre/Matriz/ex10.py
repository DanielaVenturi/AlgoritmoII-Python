
# linhas = alunos
# colunas = provas

notas = [
    [7.5, 8.0, 9.0],
    [6.0, 5.5, 7.0],
    [9.5, 8.5, 10.0]
]

for i in range(len(notas)):
    soma = 0

    for j in range(len(notas[i])):
        soma += notas[i][j]

    media = soma / len(notas[i])

    print(f"Média do aluno {i + 1}: {media:.2f}")