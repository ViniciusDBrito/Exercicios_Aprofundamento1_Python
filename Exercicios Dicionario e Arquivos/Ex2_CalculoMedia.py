def calcular_medias(notas_alunos):
    dic_medias = {}

    for chave in notas_alunos: #usando o dic sem a chave no for pega só a chave
        soma = 0
        i = 0
        for valor in notas_alunos[chave]: #usando o dic com a chave no for pega só o valor
            soma = soma + valor
            i = i + 1

        media = (soma/i)
        dic_medias[chave] = round(media,2)

    return dic_medias

notas_alunos = {
"Aluno1": [90, 85, 88],
"Aluno2": [78, 92, 87],
"Aluno3": [85, 90, 79]
}

medias_alunos = calcular_medias(notas_alunos)

print("\nNotas por aluno:", notas_alunos) 
print("Médias por aluno:", medias_alunos) 
print()