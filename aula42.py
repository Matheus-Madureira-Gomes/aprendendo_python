class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_idade_50_anos(cls, nome):
        return cls(nome, 50)
    
p1 = Pessoa.criar_idade_50_anos("Matheus")
print(p1.nome, p1.idade)