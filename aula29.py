lista = [ ]

for numero in range(10):
    lista.append(numero)


lista = [ numero for numero in range(10) ]
print(lista)


produtos = [
    {"nome": "p1", "preço": 200},
    {"nome": "p2", "preço": 20},
    {"nome": "p3", "preço": 2000},
]

novos_produtos = [
    {**produto}
    for produto in produtos
]
print(novos_produtos)

lista = [1, 2, 3, 4]

lista_nova = [x for x in range(1, 5)]
print(lista_nova)