def criar_dicionario(lista_chaves, lista_valores):
    Dic_resultados = {}
    max_list = len(lista_chaves)
    i = 0 

    while i < max_list:
        Dic_resultados[lista_chaves[i]] = lista_valores[i]
        i += 1
        
    return Dic_resultados

lista_chaves = ["A", "B", "C"]
lista_valores = [1, 2, 3]

dicionario_resultado = criar_dicionario(lista_chaves, lista_valores)

print("Lista de chaves:", lista_chaves) 
print("Lista de valores:", lista_valores)
print("Dicionário resultante:", dicionario_resultado) 