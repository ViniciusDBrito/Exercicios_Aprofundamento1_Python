def menu():
    print("\nMenu:")
    print("1 - Inserir carro.")
    print("2 - Exibir todos os carros.")
    print("3 - Exibir os carros mais velhos.")
    print("4 - Ler dados de um arquivo")
    print("5 - Gravar dados em um arquivo")
    print("6 - FIM")
    
    opc = int(input("\nInsira o setor do menu desejado: "))

    return opc


def incluir_carro(Dic_Dcarros):
    placa = input("\nInforme a placa do veículo desejado: ")
    if placa in Dic_Dcarros:
        print("O veículo já está cadastrado no sistema de carros.")
    else:
        marca = input("Informe a marca do veículo: ")
        nome = input("Informe o nome do veículo: ")
        anoC = int(input("Informe o ano do veículo: "))
        km = int(input("Informe a kilometragem do veículo: "))
        listaC = [anoC, km]
        Dic_Dcarros[placa] = [marca, nome, listaC]


def mostrar_Tcarros(Dic_Dcarros):
    max = len(Dic_Dcarros)
    if max == 0:
        print("Nenhum veículo registrado no sistema")

    else:
        somaKm = 0
        print("\nOs veículos registrados no sistema: \n")
        for chave in Dic_Dcarros:
            somaKm = somaKm + Dic_Dcarros[chave][2][1]
        
        i = 1
        for chave in Dic_Dcarros:
            print(f"Veiculo {i}:")
            print(f"A placa desse veículo é: {chave}")
            print(f"A marca desse veículo é: {Dic_Dcarros[chave][0]}")
            print(f"O nome desse veículo é: {Dic_Dcarros[chave][1]}")
            print(f"O ano desse veículo é: {Dic_Dcarros[chave][2][0]}")
            print(f"A kilometragem desse veículo é: {Dic_Dcarros[chave][2][1]}")
            print()
            
            i = i + 1
        
        print(f"A soma das kilometragens totais é: {somaKm}")
        print()



def mostrar_Mvelhos(Dic_Dcarros):
    max = len(Dic_Dcarros)
    if max == 0:
        print("Nenhum veículo registrado no sistema")
    else:
        Mvelho = 0
        for chave in Dic_Dcarros:
            if Mvelho == 0:
                Mvelho = Dic_Dcarros[chave][2][0]
            else:
                if Dic_Dcarros[chave][2][0] < Mvelho:
                    Mvelho = Dic_Dcarros[chave][2][0]
        
        print(f"\nO(s) veículo(s) mais velhos no sistema: \n")
        for chave in Dic_Dcarros:
            if Dic_Dcarros[chave][2][0] == Mvelho:
                print(f"Veículo: {Dic_Dcarros[chave][1]} ; Placa: {chave} ; Marca: {Dic_Dcarros[chave][0]} ; Ano: {Dic_Dcarros[chave][2][0]} ; KM: {Dic_Dcarros[chave][2][1]}")
        print()


def ler_arquivo(Dic_Dcarros):
    if existe_arquivo:
        arquivo = open("dic_carros.txt", "r")
        
        for linha in arquivo:
            placa, dados = linha.split("@")
            dados = dados[:-2]
            marca, modelo, ano, km = dados.split("#")
            Dic_Dcarros[placa] = [marca, modelo, [int(ano), int(km)]]
        arquivo.close()
    else:
        print("Erro, dicionário vazio!!!")
    print("Arquivo carregado com sucesso!!")
     


def gravar_arquivo(Dic_Dcarros):
    arquivo = open("dic_carros.txt", "w")
    if (len(Dic_Dcarros)) == 0:
        print("Erro, dicionário vazio!!!")
    else:
        for placa in Dic_Dcarros:
            dados = Dic_Dcarros[placa]
            linha = placa + "@" + dados[0] + "#" + dados[1] + "#" + str(dados[2][0]) + "#" + str(dados[2][1]) + "#\n"
            arquivo.write(linha)
        print("Arquivo gravado com sucesso!!")
    arquivo.close()


import os

def existe_arquivo(nome_arq):
    if os.path.exists(nome_arq):
        return True
    else:
        return False
    
Dic_Dcarros = {}
opcao = 0
while opcao != 6:
    opcao = menu()
    if opcao == 1:
        incluir_carro(Dic_Dcarros)
    elif opcao == 2:
        mostrar_Tcarros(Dic_Dcarros)
    elif opcao == 3:
        mostrar_Mvelhos(Dic_Dcarros)
    elif opcao == 4:
        ler_arquivo(Dic_Dcarros)
    elif opcao == 5:
        gravar_arquivo(Dic_Dcarros)