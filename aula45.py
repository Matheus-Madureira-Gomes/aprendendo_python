class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._frabricante = None

    @property
    def motor(self):
        return self._motor 
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor: 
     def __init__(self, nome):
        self.nome = nome

class Fabricante:
     def __init__(self, nome):
        self.nome = nome
        
onix = Carro("Celta")
chevrolet = Fabricante("Chevrolet")
motor_1 = Motor("1.0")
onix.fabricante = chevrolet
onix.motor = motor_1
print(onix.nome, onix.fabricante.nome, onix.motor.nome)

onix = Carro("Onix")
motor_1_4 = Motor("1.4")
onix.motor = motor_1_4
onix.fabricante = chevrolet
print(onix.nome, onix.fabricante.nome, onix.motor.nome)

