lista_compras = [];


while True:
    print("Selecione uma opção")
    acao = input("[i]nserir [a]pagar [l]istar ")
    acoes_permitidas = "ial"
    
    if acao in acoes_permitidas:
        if acao == "i":
            item = input("Digite um item a ser adicionado a lista ")
            lista_compras.append(item) 
    elif acao == "a":
        indice = input("Qual índice você deseja apagar ")
        try:
            indice_num = int(indice)
            del lista_compras[indice_num]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif acao == "l":
        if len(lista_compras) == 0:
            print("Lista vazia, nada a listar)")
        for i, valor in enumerate(lista_compras):
            print(i, valor)    

    else:
        print("Selecione uma opção válida")
    

