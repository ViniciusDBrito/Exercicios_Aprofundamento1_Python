def mesclar_dicionarios(dicionario1, dicionario2):
    Dic_mesclado = {}
    dicionario1.update(dicionario2)
    Dic_mesclado = dicionario1

    return Dic_mesclado

dicionario1 = {"A": 1, "B": 2, "C": 3}
dicionario2 = {"C": 4, "D": 5, "E": 6}
dicionario_mesclado = mesclar_dicionarios(dicionario1, dicionario2)

print("Dicionário 1:", dicionario1)
print("Dicionário 2:", dicionario2) 
print("Dicionário Mesclado:", dicionario_mesclado) 
