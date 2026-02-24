import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Matheus", 20 )
p2 = Pessoa("Luís", 20)
p3 = Pessoa("João", 17)    

CAMINHO_ARQUIVO = 'aula41b.json'

dados = [vars(p1), vars(p2), vars(p3)]

with open (CAMINHO_ARQUIVO, "w") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)