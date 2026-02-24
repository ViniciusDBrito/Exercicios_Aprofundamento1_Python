def chave_maior_valor(dicionario_notas):
    Dic_chaveM = {}        
    maior = 0

    for chave, valor in dicionario_notas.items(): #se no dicionario o valor for um número e não uma lista deve-se fazer o for em uma linha só 
        if valor > maior:
            maior = valor
            chaveM = chave

    Dic_chaveM = chaveM

    return Dic_chaveM

dicionario_notas = {
"Aluno1": 90,
"Aluno2": 78,
"Aluno3": 85,
"Aluno4": 92
}

chave_maior = chave_maior_valor(dicionario_notas)

print("Dicionário de notas:", dicionario_notas) 
print("Chave associada ao maior valor:", chave_maior) 