import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula58.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av Tiradentes, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. Renan Silva, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av Borussia, 33'},
]

'''

with open(CAMINHO_CSV, "w") as arquivo:
    nome_colunas = ['Nome', 'Endereço']
    escritor = csv.writer(arquivo)

    escritor.writerow(nome_colunas)

    for cliente  in lista_clientes:
        escritor.writerow(cliente.values())
'''

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)