class Carro:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

    
fusca = Carro("azul")
print(fusca.cor)