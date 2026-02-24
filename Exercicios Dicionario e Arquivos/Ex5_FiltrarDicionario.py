def filtrar_dicionario(dicionario_entrada, lista_chaves):
    Dic_saida = {}
    maxL = len(lista_chaves)
    i = 0
    while i < maxL:
        chave = lista_chaves[i]
        Dic_saida[chave] = dicionario_entrada[chave]
        i = i + 1
    
    return Dic_saida

dicionario_entrada = { 1:["A"], 2:["B","C"], 3:["D","E","F"], 4:[], 5:["G"] } 
lista_chaves = [2,4,5]

dicionario_saida = filtrar_dicionario(dicionario_entrada, lista_chaves)

print("Dicionário de entrada:", dicionario_entrada)
print("Lista de chaves para filtrar:", lista_chaves) 
print("Dicionário filtrado:", dicionario_saida) 