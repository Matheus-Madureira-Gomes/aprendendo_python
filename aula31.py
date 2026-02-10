import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = copy.deepcopy(produtos)

def aumenta_preco(lista_de_produtos):
    for item in lista_de_produtos:
        item["preco"] = round(item["preco"] * 1.10, 2)
    return lista_de_produtos

aumenta_preco(novos_produtos)

print("--- Novos Preços ---")
for produto in novos_produtos:
    print(f"{produto['nome']} : R$ {produto['preco']}")
    


